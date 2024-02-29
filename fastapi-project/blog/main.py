from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
# from . import schemas
from . import models
from database import engine

app = FastAPI()

models.Blog.metadata.create_all(engine)

class Blog(SQLModel):
    title: str
    body: str
    # published: bool


@app.post('/blog')
def create(req: Blog):
    return req
