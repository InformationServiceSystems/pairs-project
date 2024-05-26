from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class Impact(StructuredNode):

    # Attributes
    # TODO: change to IntegerProperty()
    # duration = IntegerProperty()
    duration = StringProperty(required=True) #Bsp: 9:30:00
    postcondition = StringProperty(required=True) #Bsp: Unterstützung durch befüllen und beliefern von Sandsäcken an die Feuerwehr in Bad Überkingen .

    # Relationships
    creates = Relationship(".scenario_pattern.ScenarioPattern", "t_creates")
