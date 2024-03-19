from database import engine
from sqlmodel import SQLModel, Session, select
from models.gem_model import Gem, GemProperties
import uvicorn
from main import create_db_and_tables ,app



def select_gem():
    with Session(engine) as session:
        statement = select(Gem)
        result = session.exec(statement)
        print(result.all())


select_gem()

