from sqlmodel import SQLModel, Field, create_engine, Session, select, Column


class Base(SQLModel, table=True):
    id:int = Field(int, primary_key=True, index=True)
    title:str = Field(str)
    body:str = Field(str)
