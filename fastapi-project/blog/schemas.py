from sqlmodel import SQLModel


class Blog1(SQLModel):
    title: str
    body: str
    # published: bool
