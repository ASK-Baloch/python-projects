from sqlmodel import SQLModel, Field ,Relationship
from enum import Enum, IntEnum
from typing import Optional


class GemTypes(str, Enum):
    DIAMOND = "DIAMOND"
    RUBY = 'RUBY'
    EMERALD = 'EMERALD'


class GeoClarity(IntEnum):
    SI = 1
    VS = 2
    WS = 3
    FL = 4


class GemColor(str, Enum):
    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    I = "I"


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    size: float = 1
    clarity: Optional[GeoClarity] = None
    color: Optional[GemColor] = None


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    price: float
    available: bool = True
    gem_type: GemTypes = GemTypes.DIAMOND

    # gem_properties: Optional[GemProperties] = Field(
    #     default=None, foreign_key="gemproperties.id")
    
    gem_properties: Optional[GemProperties] = Relationship(back_populates="gems")  # type: ignore # Use Relationship for relationships


# Define the back-reference for clarity
GemProperties: Optional[Gem] = Relationship(back_populates="gem_properties")
