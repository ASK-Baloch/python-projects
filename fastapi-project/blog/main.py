from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
from .schemas import Blog
from .models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(engine)

# class Blog(SQLModel):
#     title: str
#     body: str
#     # published: bool


@app.post('/blog')
def create(req: Blog):
    return req
