from sqlmodel import SQLModel, Field, Relationship
from typing import List , Optional


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(str)
    email: str = Field(str)
    password: str = Field(str)
    user_id:int = Field(foreign_key="user.id")
    creator:List["Blog"] = Relationship(back_populates="Blog")


class ShowUser(SQLModel):
    name: str
    email: str


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    body: str
    # published: bool
    blogs:Optional[User] = Relationship(back_populates="creator")


class showBlog(SQLModel):
    title: str