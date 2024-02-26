from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated, Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI(
    title="Location Finder API",
    version="1.0.0",
    servers=[
        {
            # ADD NGROK URL Here Before Creating GPT Action
            "url": "https://jay-correct-physically.ngrok-free.app",
            "description": "Production Server"
        },
        {
            "url": "http://localhost:8000",  # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ])


class Location(SQLModel, table=True):
    # id:Optional[int] = Field(default=None,primary_key=True)
    name: str = Field(index=True, primary_key=True)
    location: str


database_url = "postgresql://realstar5525:X1ln2pUotjGS@ep-white-bird-a5870a9e.us-east-2.aws.neon.tech/sqlmodal?sslmode=require"

# connect_args = {"check_same_thread": False}
engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# dependency function


@app.post("/person/")
def create_person(person_data: Location):
    with Session(engine) as session:
        session.add(person_data)
        session.commit()
        session.refresh(person_data)
        return person_data


@app.get("/persons/")
def read_all_persons():
    with Session(engine) as session:
        loc_data = session.exec(select(Location)).all()
        return loc_data

# dependency function


def get_location_or_404(name: str) -> Location:
    with Session(engine) as session:
        low_name = name.lower()
        loc_data = session.exec(select(Location).where(
            Location.name == low_name)).first()
        if not loc_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"No location found for {name}")
        return loc_data

@app.get("/location/{name}")
def get_person_location(name: str, location: Annotated[Location, Depends(get_location_or_404)]):
    print("hello world")
    return location
