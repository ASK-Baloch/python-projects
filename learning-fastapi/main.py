from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
import uvicorn


app = FastAPI()


@app.get('/')
def index():
    return {'data': {
        'name': 'Ahmed'
    }}


@app.get('/about')
def about():
    return {'data': 'about title'}
