from fastapi import FastAPI
import uvicorn
from database import engine
from sqlmodel import SQLModel
from models.gem_model import *

app = FastAPI()

# this function create tables in database and bring models into tables


def create_db_and_tables():
    Gem.metadata.create_all(engine)

# this is a route that is a get method that returns a string upon calling


@app.get('/')
def hello():
    return 'Hello, world!'


# this is a condition that if the file name is main. then run server and call the functin relatable to creating tables
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    create_db_and_tables()
