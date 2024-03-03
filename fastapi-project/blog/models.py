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
