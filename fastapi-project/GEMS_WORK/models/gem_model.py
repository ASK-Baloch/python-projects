from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional


class GemTypes(Enum):
    DIAMOND = "DIAMOND"
    RUBY = 'RUBY'
    EMERALD = 'EMERALD'

class GeoClarity(Enum):
    SI = 1
    VS = 2 
    WS = 3 
    FL = 4


class GemColor(Enum):
    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    I = "I"

class GemProperties(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    size:float =1
    clarity: Optional[GeoClarity] = None
    color: Optional[GemColor] = None


class Gem(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    price: float
    available: bool = True
    gem_type = GemTypes = GemTypes.DIAMOND

    gem_properties: Optional[GemProperties] = Field(default=None, foreign_key="gemproperties.id")
