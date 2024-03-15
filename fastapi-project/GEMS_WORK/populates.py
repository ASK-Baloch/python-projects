from models.gem_model import Gem, GemProperties
import random
import string
color_grades=string.ascii_uppercase[3:9]

def create_gem_props():
    size = random.randInt(3, 70)/10
    color = color_grades(random.randint(0,5))
    clarity = random.randint(1,4)
    gem_p=GemProperties(size=size,color=color,clarity=clarity)
    return gem_p

def create_gem():
    gem = Gem(price=1000,gem_properties_id=gem_p)
    return gem

def create_gems_db():
    # for i in range(10):
    #     gem_p = create_gem_props()
    #     gem = create_gem()
    #     gem_p.gems.append(gem)
    #     gem.gem_properties = gem_p
    #     gem_p.save()
    #     gem.save()