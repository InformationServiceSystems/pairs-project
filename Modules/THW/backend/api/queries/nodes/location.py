from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Location(StructuredNode):

    # Relationships
    regional_area = StringProperty(required=True)
    federal_state = StringProperty(required=True)
    city =  StringProperty(required=True)
    country = StringProperty(required=True)
    street = StringProperty(required=True)
    local_association = StringProperty(required=True)

    # Relationships
    happens_at = Relationship(".scenario_pattern.ScenarioPattern", "t_happens_at")
    lives_at = Relationship(".person.Person", "t_lives_at")
