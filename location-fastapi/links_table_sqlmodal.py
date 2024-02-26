from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
from os import getenv

_: bool = load_dotenv(find_dotenv())


class HeroTeamLink(SQLModel, table=True):
    hero_id: Optional[int] = Field(
        default=None, foreign_key="teamhero.id", primary_key=True)
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True)


class Team(SQLModel, table=True):
    """
    create a Team Table with colums: id, name, headquarters.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    headquarters: str
    heros: List["TeamHero"] = Relationship(back_populates="team", link_model=HeroTeamLink)


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
    teams: Optional[Team] = Relationship(back_populates="heros", link_model=HeroTeamLink)


# database_connection_str = "postgresql://realstar5525:X1ln2pUotjGS@ep-white-bird-a5870a9e.us-east-2.aws.neon.tech/sqlmodal?sslmode=require"
postgres_url: str = getenv("POSTGRESQL_URL")  # type: ignore
engine = create_engine(postgres_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        team_xman = Team(name="X-MEN", headquarters="X Tower")
        team_titans = Team(name="Team Titans",headquarters="Titans Place")
        # session.add(team_avengers)
        # session.add(team_justice_league)
        # # session.commit()

        hero_logan = TeamHero(id=4, name="wolverine",secret_name="Logan",teams=[team_xman , team_titans]) # type: ignore
        hero_tommy = TeamHero(id=6, name="Rusty-Man", secret_name="Tommy sharp",teams=[team_titans]) # type: ignore
        session.add_all([hero_logan, hero_tommy])

        # hero_superman = TeamHero(name="Superman", secret_name="Clark Kent", age=35, team_id=team_justice_league.id)
        # hero_iron_man = TeamHero(name="Iron Man", secret_name="Tony Stark", team_id=team_avengers.id)
        # hero_spider_man = TeamHero(name="Spiderman", secret_name = "Peter Parker")
        # session.add(hero_superman)
        # session.add(hero_iron_man)
        # session.add(hero_spider_man)
        session.commit()
        session.close()


def create_teams_and_heroes():
    with Session(engine) as session:
        hero_black_widow = TeamHero(
            name="Black Widow", secret_name="Natasha Romanoff", age=35)
        hero_black_panther = TeamHero(
            name="Black Panther", secret_name="T'Challa", age=35)
        team = Team(name="DarthVaders", headquarters="Galaxy Station",
                    heros=[hero_black_widow, hero_black_panther])
        session.add(team)
        session.commit()
        session.close()


def get_heroes():
    with Session(engine) as session:
        statement = select(Team).where(Team.name == "Avengers")
        team = session.exec(statement).first()
        print("Selected Team is : ", team)
        print("Selected Team heroes are: ", team.heros)  # type:ignore
        session.close()


def update_heroes():
    with Session(engine) as session:
        statement = select(Team).where(Team.name == "Avengers")
        team = session.exec(statement).first()
        statement1 = select(TeamHero).where(TeamHero.name == "Spiderman")
        hero = session.exec(statement1).first()
        hero.team = team  # type:ignore
        session.add(hero)
        session.commit()
        session.close()


def delete_heroes():
    with Session(engine) as session:
        statement = select(Team).where(Team.name == "X-MEN")
        team = session.exec(statement).first()
        statement1 = select(TeamHero).where(TeamHero.name == "Spiderman")
        hero = session.exec(statement1).first()
        hero.team = None  # type: ignore
        session.add(hero)
        session.commit()
        session.close()


if __name__ == "__main__":
    # create_db_and_tables()
    create_heroes()
    # create_teams_and_heroes()
    # get_heroes()
    # update_heroes()
    # delete_heroes()
