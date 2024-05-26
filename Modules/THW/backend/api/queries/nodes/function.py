from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
from pathlib import Path

#===============================================================================
# Neo4j Model Class
#===============================================================================
class Function(StructuredNode):

    # Attributes
    name = StringProperty(required=True) #Bsp: Gruppenführer oder Sprachfunker
    number = IntegerProperty() #Bsp: 5

    # Relationships
    requires = Relationship(".qualifications.Qualifications", "t_requires")
    has_additional_function = Relationship(".additional_function.AdditionalFunction", "t_has_additional_function")
    composed_of = Relationship(".unit.Unit", "t_composed_of")
    executes = Relationship(".person.Person", "i_executes")
