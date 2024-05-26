from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Unit(StructuredNode):

    # Attributes
    name = StringProperty(required=True) #Bsp: Bergungsgruppe
    description = StringProperty(required=True) #Bsp: Die Bergungsgruppe ist eine universell einsetzbare Teileinheit im Technischen Zug
    strength = StringProperty(required=True) #Bsp: "-/2/7/9 (+9)"
    # characteristics = StringProperty() #Bsp: Schweiß- und Brennschneidegerät
    abbreviation = StringProperty(required=True) #Bsp: "B"

    # Relationships
    # vehicle = RelationshipTo("Vehicle", "can_use")
    # task = RelationshipTo("Task", "can_fulfill")
    # role = RelationshipTo("Role", "assumes_role")
    composed_of = Relationship(".function.Function", "t_composed_of")
    assigned_to = Relationship(".person.Person", "i_assigned_to")
    consists_of = Relationship(".actor.Actors", "i_consists_of")
    fulfills = Relationship(".action.Action", "t_fulfills")
    uses = Relationship(".equipment.Equipment", "t_uses")
    drives = Relationship(".vehicle.Vehicle", "t_drives")
