from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional


class GeoClarity(Enum):
    FL = "FL"
    VS = 'VS'
    WS = 'WS'
    SI = 'SI'


class GemColor(Enum):
    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    I = "I"


class Gem(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    size: float = 1
    name: str
    description: str
    price: float
    clarity: Optional[GeoClarity] = None
    color: Optional[GemColor] = None
