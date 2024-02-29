from fastapi import FastAPI
from schemas import Blog


app = FastAPI()


@app.post('/blog')
def create(req: Blog):
    return req
