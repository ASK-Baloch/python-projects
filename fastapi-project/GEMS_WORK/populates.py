from models.gem_model import Gem, GemProperties
import random
import string

# creating a list of colors
color_grades=string.ascii_uppercase[3:9]


# creating gem props to further use like an interface
def create_gem_props():
    size = random.randInt(3, 70)/10
    color = color_grades(random.randint(0,5))
    clarity = random.randint(1,4)
    gem_p=GemProperties(size=size,color=color,clarity=clarity)
    return gem_p


# funtion that will be used to create a gem
def create_gem(gem_p):
    gem = Gem(price=1000,gem_properties_id=gem_p)
    return gem

# funtion that will be used to create tables in database
def create_gems_db():
    # for i in range(10):
    #     gem_p = create_gem_props()
    #     gem = create_gem()
    #     gem_p.gems.append(gem)
    #     gem.gem_properties = gem_p
    #     gem_p.save()
    #     gem.save()