from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Vehicle(StructuredNode):

    # Attributes Equipment
    name = StringProperty(required=True) # Bsp: Gerätekraftwagen

    #Vehicles
    #name: Gerätekraftwagen (7 t Nutzlast)

    # Relationships
    drives = Relationship(".unit.Unit", "t_drives")
