from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Subevent(StructuredNode):

    name = StringProperty(required=True)

    # Relationships
    belongs_to = Relationship(".event.Event", "s_belongs_to")
    identified_by  = Relationship(".scenario_pattern.ScenarioPattern", "t_identified_by")
    has_subtask = Relationship(".subtask.Subtask", "t_has_subtask")

