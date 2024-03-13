from fastapi import FastAPI
import uvicorn
from database import engine
from sqlmodel import create_engine,SQLModel

app = FastAPI()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



@app.get('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    create_db_and_tables()