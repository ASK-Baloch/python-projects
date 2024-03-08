from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


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


# class User(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(max_length=255)  # Enforce a reasonable length for names
#     email: str = Field(max_length=255, unique=True)  # Ensure unique emails
#     password: str = Field(..., nullable=False)  # Hide password on retrieval
#     blogs: Relationship("Blog", back_populates="creator")  # type:ignore


# class Blog(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     # Enforce a reasonable length for titles
#     title: str = Field(max_length=255)
#     body: str = Field(..., nullable=True)  # Allow body to be optional
#     creator_id: int = Field(default=None, foreign_key="user.id")
#     # Relationship back-reference
#     creator: User = Relationship(back_populates="blogs")

# class User(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(max_length=255)
#     email: str = Field(max_length=255, unique=True)
#     password: str = Field(..., nullable=False)  # Hide password on retrieval
#     # Many-to-Many relationship
#     blogs = Relationship(Blog, back_populates="creator")

#     # ... other methods (password setter, etc.)


# class Blog(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str = Field(max_length=255)
#     body: str = Field(..., nullable=True)
#     creator_id: int = Field(default=None, foreign_key="user.id")
#     creator: User = Relationship(
#         User, back_populates="blogs")  # Back-reference
