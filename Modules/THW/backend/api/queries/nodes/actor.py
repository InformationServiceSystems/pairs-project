from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================

class Actors(StructuredNode):

    # Attributes
    number_of_helpers = IntegerProperty(required=True) # Bsp: 10
    duty_hours = IntegerProperty(required=True) # Bsp: 80

    # Relationships
    # mission = RelationshipTo("Mission", "takes")
    # unit = RelationshipTo("Unit", "are")
    involves = Relationship(".scenario_pattern.ScenarioPattern", "t_involves")
    consists_of = Relationship(".unit.Unit", "i_consists_of")
    fulfills = Relationship(".subtask.Subtask", "t_fulfills")
