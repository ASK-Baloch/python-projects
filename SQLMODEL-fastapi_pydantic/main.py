from fastapi import FastAPI, Depends , HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from dotenv import load_dotenv, find_dotenv
from os import getenv

from typing import Annotated

_: bool = load_dotenv(find_dotenv())

class VillainBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str

class Villan(VillainBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    age: int | None = None
    

class VillainCreate(VillainBase):
    age: int | None = None


class VillainResponse(VillainBase):
    id: int
    age: int | None = None

class VillainUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None

postgres_url: str = getenv("POSTGRESQL_URL")
engine = create_engine(postgres_url)


def create_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

# DB DEpendency Injecion


def get_deb():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/villains", response_model=list[Villan])
def get_villains(session: Annotated[Session, Depends(get_deb)]):
    villains = session.exec(select(Villan)).all()
    return villains


@app.post("/villains", response_model=VillainResponse)
def create_villain(villain: VillainCreate, db: Annotated[Session, Depends(get_deb)]):
    print("DATA FROM CLIENT", villain)
    hero_to_insert = Villan.model_validate(villain)
    print("Data after validation", hero_to_insert)
    db.add(hero_to_insert)
    db.commit()
    db.refresh(hero_to_insert)
    return hero_to_insert


@app.get("/villains/{villain_id}", response_model=VillainResponse)
def get_villain(villain_id: int, session: Annotated[Session, Depends(get_deb)]):
    villain = session.get(Villan, villain_id)
    if not villain:
        raise HTTPException(status_code=404, detail="Villain not found")
    return villain

@app.patch("/villains/{villain_id}", response_model=VillainResponse)
def update_villian(villain_id: int, session: Annotated[Session, Depends(get_deb)], villain_data: VillainUpdate):
    villain = session.get(Villan, villain_id)
    if not villain:
        raise HTTPException(status_code=404, detail="Villain not found")
    print("VILLAIN IN DB" , villain)
    print("DATA FROM CLIENT" , villain_data)
    villain_dict_data = villain_data.model_dump(exclude_unset=True)
    print("villain_dict_data", villain_dict_data)
    for key, value in villain_dict_data.items():
        setattr(villain, key, value)
    print("AFTER ", villain)

    session.add(villain)
    session.commit()
    session.refresh(villain)
    return villain
