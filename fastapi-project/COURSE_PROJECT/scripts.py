from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
from os import getenv
import json

_: bool = load_dotenv(find_dotenv())


postgres_url: str = getenv("DATABASE_URL")  # type: ignore


class Course(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, nullable=False)
    chapters: str = Field(default="", sa_column_kwargs={"type": "JSONB"})
    rating: dict = Field(default={"total": 0, "count": 0})


# Connect to PostgreSQL database
engine = create_engine(postgres_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Read courses from courses.json
with open("courses.json", "r") as f:
    courses = json.load(f)

# Add rating field to each course and chapter
for course in courses:
    course["chapters"] = [{"rating": {"total": 0, "count": 0}} for _ in course["chapters"]]
    course["rating"] = {"total": 0, "count": 0}

# Insert courses into table
with Session(engine) as session:
    for course in courses:
        course_obj = Course(name=course["name"], chapters=json.dumps(course["chapters"]))
        session.add(course_obj)
    session.commit()

    session.exec("CREATE INDEX idx_course_name ON courses USING GIN(name)")
    session.commit()

print("Courses data successfully imported into PostgreSQL.")