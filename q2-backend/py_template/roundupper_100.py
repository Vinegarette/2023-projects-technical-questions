from dataclasses import dataclass
from enum import Enum
from typing import Union, NamedTuple, List
from flask import Flask, request, Response
from math import sqrt
from json import dumps
URL = 'localhost:8080'

# SpaceCowboy models a cowboy in our super amazing system
@dataclass
class SpaceCowboy:
    name: str
    lassoLength: int

# SpaceAnimal models a single animal in our amazing system
@dataclass
class SpaceAnimal:
    # SpaceAnimalType is an enum of all possible space animals we may encounter
    class SpaceAnimalType(Enum):
        PIG = "pig"
        COW = "cow"
        FLYING_BURGER = "flying_burger"

    type: SpaceAnimalType

# SpaceEntity models an entity in the super amazing (ROUND UPPER 100) system
@dataclass
class SpaceEntity:
    class Location(NamedTuple):
        x: int
        y: int

    metadata: Union[SpaceCowboy, SpaceAnimal]
    location: Location
    
# === Helper Function ===

def in_range(cowboy, animal):
    lasso_length = cowboy.metadata.lassoLength
    c_x, c_y = int(cowboy.location['x']), int(cowboy.location['y'])
    a_x, a_y = int(animal.location['x']), int(animal.location['y'])
    return lasso_length >= sqrt((c_x - a_x)**2 + (c_y - a_y)**2)

# ==== HTTP Endpoint Stubs ====
app = Flask(__name__)
space_database: List[SpaceEntity] = []

# the POST /entity endpoint adds an entity to your global space_database
@app.route('/entity', methods=['POST'])
def create_entity():
    entities = request.get_json()
    for info in entities['entities']:
        # Could edit the entity class/create a factory class in case there are more space_entities added later
        type = info['type']
        metadata = info['metadata']
        location = info['location']
        # Create a new SpaceEntity
        if type == 'space_cowboy':
            space_database.append(SpaceEntity(SpaceCowboy(metadata['name'], metadata['lassoLength']), location))
        elif type == 'space_animal':
            space_database.append(SpaceEntity(SpaceAnimal(metadata['type']), location))
        
        
    return Response(status=200)
       

@app.route('/list', methods=['GET'])
def list_entities():
    # For testing purposes...
    return space_database

# lasooable returns all the space animals a space cowboy can lasso given their name
@app.route('/lassoable', methods=['GET'])
def lassoable():
    
    info = request.get_json()
    # Search through the list of SpaceEntites 
    name = info['cowboy_name']
    cowboy = [entity for entity in space_database if type(entity.metadata) == SpaceCowboy and entity.metadata.name == name]
    if len(cowboy) == 0:
        print(f"Failed to find a cowboy with name {name}")
        return Response(status=400)
    
    cowboy = cowboy[0]
    animals = [animal for animal in space_database if type(animal.metadata) == SpaceAnimal and in_range(cowboy, animal)]
    
    
    # Formatting 
    res = []
    for animal in animals:
        res.append({
            "type" : animal.metadata.type,
            "location" : {
                "x" : animal.location['x'],
                "y" : animal.location['y']
            }
        })
    
    print({"space_animals" : res})
    return Response(status=200)
    

# DO NOT TOUCH ME, thanks :D
if __name__ == '__main__':
    app.run(debug=True, port=8080)