from fastapi import FastAPI
from schemas import Blog1
from models import Base
from database import engine




# Create all tables
Base.metadata.create_all(engine)

# Create the FastAPI application
app = FastAPI()


@app.post('/blog')
def create(req: Blog1):
    print("Blog Title", Blog1.title)
    return req
