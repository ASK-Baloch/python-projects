from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from dotenv import load_dotenv , find_dotenv
from os import getenv

_:bool = load_dotenv(find_dotenv())


class SuperHero(SQLModel, table=True):
    """
    Create a Hero Table with columns: id, name, secret_name, age, team_id.
    foreign Key: team_id refreneces id in Team table.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


# database_connection_str = "postgresql://realstar5525:X1ln2pUotjGS@ep-white-bird-a5870a9e.us-east-2.aws.neon.tech/sqlmodal?sslmode=require"
postgres_url : str = getenv("POSTGRESQL_URL")  # type: ignore
engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_hero():
    hero_1 = SuperHero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = SuperHero(name="Spider", secret_name="Peter Parker")
    hero_3 = SuperHero(name="Batman", secret_name="Bruce Wayne")
    session = Session(engine)
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
    session.close()


def get_hero():
    session = Session(engine)
    statement = select(SuperHero.id , SuperHero.name)
    # statement = select(SuperHero).where(SuperHero.name == "Batman").where(SuperHero.age == None)
    # statement = select(SuperHero).where(SuperHero.name == "Batman").offset(4).limit(2)
    result = session.exec(statement)
    print(result.all())
    # for hero in result:
    #     print(hero.name)


def update_hero():
    session = Session(engine)
    statement = select(SuperHero).where(SuperHero.name == "Deadpond")
    result = session.exec(statement).first()
    print(result)
    result.age = 39
    session.add(result) 
    session.commit()
    session.close()
    print("age updated")
    print(result)

def delete_hero():
    session = Session(engine)
    statement = select(SuperHero).where(SuperHero.id == 6)
    result = session.exec(statement).first()
    print(result)
    session.delete(result)
    session.commit()
    session.close()

if __name__ == "__main__":
    create_db_and_tables()
    # create_hero()
    get_hero()
    # update_hero()
    # delete_hero()
