from sqlmodel import SQLModel, Field


# class Blog1(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str = Field(str)
#     body: str = Field(str)

# from schemas import Base


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    body: str
    # published: bool


class showBlog(SQLModel):
    title: str


# class User(SQLModel):
#     name: str
#     email: str
#     password: str


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(str)
    email: str = Field(str)
    password: str = Field(str)

class ShowUser(SQLModel):
    name:str
    email:str