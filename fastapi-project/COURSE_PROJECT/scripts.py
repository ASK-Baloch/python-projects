from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
from os import getenv
import json

_: bool = load_dotenv(find_dotenv())


postgres_url: str = getenv("DATABASE_URL")  # type: ignore


class course(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, nullable=False)
    chapters: str = Field(default="", sa_column_kwargs={"type": "JSONB"})
    rating: dict = Field(default={"total": 0, "count": 0})

