from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class ScenarioPattern(StructuredNode):

    # id = StringProperty(required=True)
    start_date = StringProperty(required=True)
    end_date = StringProperty(required=True)

    # Relationships
    identified_by  = Relationship(".subevent.Subevent", "t_identified_by")
    bounded_by = Relationship(".context.Context", "t_bounded_by")
    described_by = Relationship(".provenance.Provenance", "t_described_by")
    caused_by = Relationship(".reason.Reason", "t_caused_by")
    creates = Relationship(".impact.Impact", "t_creates")
    happens_at = Relationship(".location.Location", "t_happens_at")
    involves = Relationship(".actor.Actors", "t_involves")
