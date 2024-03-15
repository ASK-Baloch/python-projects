from main import engine
from sqlmodel import SQLModel, Session , select
from models.gem_model import Gem,GemProperties

def select_gem():
    with Session as session:
        statement = select(Gem)
        result = session.exec(statement)
        
        return statement