from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Action(StructuredNode):
    
    # id = StringProperty(required=True)
    name = StringProperty(required=True)
    description = StringProperty(required=True)
    category = StringProperty(required=True)

    # Relationships
    fulfills = Relationship(".unit.Unit", "t_fulfills")
    subordinated = Relationship(".subtask.Subtask", "s_subordinated")
    consists_of = Relationship(".actiontype.ActionType", "s_consists_of")
