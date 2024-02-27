from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select


app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/{id}')
def abc(id):
    return {'Blog No': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': f'blog comments: {id}'}
    # return {'data': {'1', '2'}}
