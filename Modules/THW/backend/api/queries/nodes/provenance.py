from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Provenance(StructuredNode):

    planner = StringProperty(required=True) #Bsp: OV Aachen
    requester = StringProperty(required=True) #Bsp: Feuerwehr

    # Relationships
    described_by = Relationship(".scenario_pattern.ScenarioPattern", "t_described_by")
