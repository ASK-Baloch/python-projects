from fastapi import FastAPI
from sqlmodel import SQLModel

from sqlmodel import SQLModel, Field, create_engine, Session, select, Column
# from database import engine
from dotenv import load_dotenv, find_dotenv
from os import getenv

from typing import Annotated

_: bool = load_dotenv(find_dotenv())


postgres_url: str = getenv("POSTGRESQL_URL")
engine = create_engine(postgres_url)


class Base(SQLModel, table=True):
    id = Column(int, primary_key=True, index=True)
    title = Column(str)
    body = Column(str)


class Blog(SQLModel):
    title: str
    body: str
    # published: bool


Base.metadata.create_all(engine)

app = FastAPI()


@app.post('/blog')
def create(req):
    return req
