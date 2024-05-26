from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class Qualifications(StructuredNode):

    name = StringProperty(required=True)

    # Relationships
    has_qualification = Relationship(".person.Person", "t_has_qualification")
    requires = Relationship(".function.Function", "t_requires")
    requires_qualification = Relationship(".additional_function.AdditionalFunction", "t_requires_qualification")
