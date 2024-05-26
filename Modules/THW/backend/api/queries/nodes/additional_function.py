from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class AdditionalFunction(StructuredNode):

    # Attributes
    name = StringProperty(required=True) #Bsp: Gruppenführer oder Sprachfunker
    number = IntegerProperty() #Bsp: 5

    # Relationships
    requires_qualification = Relationship(".qualifications.Qualifications", "t_requires_qualification")
    has_additional_function = Relationship(".function.Function", "t_has_additional_function")
