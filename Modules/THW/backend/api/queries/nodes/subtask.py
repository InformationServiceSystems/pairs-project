from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Subtask(StructuredNode):

    # Attributes
    name = StringProperty(required=True) #Bsp: Bergungsgruppe

    # Relationships
    # vehicle = RelationshipTo("Vehicle", "can_use")
    # task = RelationshipTo("Task", "can_fulfill")
    # role = RelationshipTo("Role", "assumes_role")
    fulfills = Relationship(".actor.Actors", "t_fulfills")
    subordinated = Relationship(".action.Action", "s_subordinated")
    belongs_to = Relationship(".actiontype.ActionType", "t_belongs_to")
    has_subtask = Relationship(".subevent.Subevent", "t_has_subtask")
