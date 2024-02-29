from sqlmodel import SQLModel


class Blog(SQLModel):
    title: str
    body: str
    # published: bool
