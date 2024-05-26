from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class ActionType(StructuredNode):

    name = StringProperty(required=True)

    # Relationships
    belongs_to = Relationship(".subtask.Subtask", "t_belongs_to")
    consists_of = Relationship(".action.Action", "s_consists_of")
