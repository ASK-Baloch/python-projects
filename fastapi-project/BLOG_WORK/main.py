from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select


app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'Blog No': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': f'blog comments: {id} ' f'{limit}'}
    # return {'data': {'1', '2'}}

class Blog(SQLModel):
    title: str
    body:  str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f'Blog is created successfully with title as {blog.title}'}

