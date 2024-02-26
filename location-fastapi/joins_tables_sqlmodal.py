from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from typing import Optional
from dotenv import load_dotenv, find_dotenv
from os import getenv

_: bool = load_dotenv(find_dotenv())


class Team(SQLModel, table=True):
    """
    create a Team Table with colums: id, name, headquarters.
    """
    id: Optional[int] = Field(primary_key=True)
    name: str
    headquarters: str


class TeamHero(SQLModel, table=True):
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
postgres_url: str = getenv("POSTGRESQL_URL")  # type: ignore
engine = create_engine(postgres_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        team_avengers = Team(
            name="Avengers", headquarters="Avengers Mansion")  # type: ignore
        team_justice_league = Team(
            name="Justice League", headquarters="Hall of Justice")  # type: ignore
        # session.add(team_avengers)
        # session.add(team_justice_league)
        # session.commit()

        hero_superman = TeamHero(
            name="Superman", secret_name="Clark Kent", age=35, team_id=team_justice_league.id)
        hero_iron_man = TeamHero(
            name="Iron Man", secret_name="Tony Stark", team_id=team_avengers.id)
        hero_spider_man = TeamHero(
            name="Spiderman", secret_name="Peter Parker")
        # session.add(hero_superman)
        # session.add(hero_iron_man)
        session.add(hero_spider_man)
        session.commit()
        session.close()


def get_heroes():
    with Session(engine) as session:
        """with Where . for small queries """
        # statement = select(TeamHero).where(TeamHero.team_id == 2)
        # result = session.exec(statement)
        # heroes = result.all()
        # print("Heroes:",heroes)

        """with join . for big data. Always not recommended because it will return all the data from the table thus it burdens db"""
        statement = select(TeamHero).join(Team)
        result = session.exec(statement)
        heroes = result.all()
        print("Heroes:", heroes)


def update_heroes():
    session = Session(engine)
    statement = select(TeamHero).where(TeamHero.name == "Spiderman")
    result = session.exec(statement).first()
    result.team_id = 1  # type: ignore
    session.add(result)
    session.commit()
    session.close()
    print("team updated")

# def delete_hero():
#     session = Session(engine)
#     statement = select(Hero).where(Hero.id == 6)
#     result = session.exec(statement).first()
#     print(result)
#     session.delete(result)
#     session.commit()
#     session.close()


if __name__ == "__main__":
    # create_db_and_tables()
    # create_heroes()
    # get_heroes()
    update_heroes()
    # delete_hero()
