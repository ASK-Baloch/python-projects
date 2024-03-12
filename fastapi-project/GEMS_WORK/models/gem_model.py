from sqlmodel import SQLModel, Field

class Gem(SQLModel, table=True):
    id: int = Field(primary_key=True,index=True)
    size:float = 1
    name: str
    description: str
    price: float
