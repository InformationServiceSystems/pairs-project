from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Context(StructuredNode):

    # Attributes
    description = StringProperty(required=True) # Bsp: Einsatz oder sonstige technische Hilfsleistung

    # Relationships
    bounded_by = Relationship(".scenario_pattern.ScenarioPattern", "t_bounded_by")
