from models.gem_model import Gem, GemProperties
import random
import string
from main import engine
from sqlmodel import SQLModel, Session
# creating a list of colors
color_grades = string.ascii_uppercase[3:9]


# creating gem props to further use like an interface
def create_gem_props():
    size = random.randInt(3, 70)/10
    color = color_grades(random.randint(0, 5))
    clarity = random.randint(1, 4)
    gem_p = GemProperties(size=size, color=color, clarity=clarity)
    return gem_p


# funtion that will be used to create a gem
def create_gem(gem_p):
    gem = Gem(price=1000, gem_properties_id=gem_p)
    return gem

# funtion that will be used to create tables in database


def create_gems_db():
    gem_p = create_gem_props()
    print(gem_p)
    with Session(engine) as session:
        session.add(gem_p)
        session.commit()
        g = create_gem(gem_p.id)
        session.add(g)
        session.commit()
        session.close()

create_gems_db