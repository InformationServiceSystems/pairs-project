from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class Reason(StructuredNode):

    # Attributes
    precondition = StringProperty(required=True) #Bsp: Starkregen

    # Relationships
    caused_by = Relationship(".scenario_pattern.ScenarioPattern", "t_caused_by")
