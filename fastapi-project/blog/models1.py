from sqlmodel import SQLModel, Field, Relationship
from models import User


# class Base(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str = Field(str)
#     body: str = Field(str)


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # Enforce a reasonable length for titles
    title: str = Field(max_length=255)
    body: str = Field(..., nullable=True)  # Allow body to be optional
    creator_id: int = Field(default=None, foreign_key="user.id")
    # Relationship back-reference
    creator: User = Relationship(User, back_populates="blogs")
