from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select, Column
from dotenv import load_dotenv, find_dotenv
from os import getenv
from schemas import Blog1

# Load environment variables
load_dotenv(find_dotenv())

# Get the PostgreSQL URL from environment variables
postgres_url: str = getenv("POSTGRESQL_URL")

# Create the SQLModel engine
engine = create_engine(postgres_url)

# Define the base model



class Base(SQLModel, table=True):
    id:int = Field(int, primary_key=True, index=True)
    title:str = Field(str)
    body:str = Field(str)

# Define the Blog model


class Blog(Base):
    pass


# Create all tables
Base.metadata.create_all(engine)

# Create the FastAPI application
app = FastAPI()


@app.post('/blog')
def create(req: Blog1):
    print("Blog Title" , Blog1.title)
    return req
