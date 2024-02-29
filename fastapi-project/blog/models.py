from sqlmodel import SQLModel, Field, create_engine, Session, select ,Column

class Blog(SQLModel , table = True):
    id= Column(int , primary_key= True, index = True)
    title = Column(str)
    body = Column(str)