from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from models import Blog
from database import engine
from typing import Annotated


# Create the FastAPI application
app = FastAPI()

# Create all tables
Blog.metadata.create_all(engine)


def get_deb():
    with Session(engine) as session:
        yield session


@app.post('/blog')
def create(req: Blog, db: Session = Depends(get_deb)):
    new_blog = Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog")
def get_all(db: Annotated[Session, Depends(get_deb)]):
    blogs = db.exec(select(Blog)).all()
    return blogs
