from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Event(StructuredNode):

    name = StringProperty(required=True)
    hazard_type= StringProperty(required=True)

    # Relationships
    belongs_to = Relationship(".subevent.Subevent", "s_belongs_to")

