from sqlmodel import create_engine
from dotenv import load_dotenv, find_dotenv
from os import getenv

from typing import Annotated

_: bool = load_dotenv(find_dotenv())


postgres_url: str = getenv("POSTGRESQL_URL")
engine = create_engine(postgres_url,echo=True)