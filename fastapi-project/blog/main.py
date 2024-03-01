from fastapi import FastAPI
from sqlmodel import SQLModel

# from sqlmodel import SQLModel, Field, create_engine, Session, select ,Column
# from database import engine


# class Base(SQLModel , table = True):
#     id= Column(int , primary_key= True, index = True)
#     title = Column(str)
#     body = Column(str)


# class Blog(SQLModel):
#     title: str
#     body: str
#     # published: bool

# Base.metadata.create_all(engine)

app = FastAPI()


@app.post('/blog')
def create(req):
    return req
