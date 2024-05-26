from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Equipment(StructuredNode):

    # Attributes Equipment
    name = StringProperty(required=True) # Bsp: Gerätekraftwagen
    number = IntegerProperty(required=True) #Bsp: 1

    #Vehicles
    #name: Gerätekraftwagen (7 t Nutzlast)

    # Relationships
    uses = Relationship(".unit.Unit", "t_uses")
