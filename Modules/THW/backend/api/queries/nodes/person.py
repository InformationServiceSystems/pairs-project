from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import IntegerProperty
from neomodel import BooleanProperty
from neomodel import Relationship
#===============================================================================
# Neo4j Model Class
#===============================================================================
class Person(StructuredNode):

    # Attributes
    # id = StringProperty(required=True)
    age = IntegerProperty(required=True) # Bsp: 57
    gender = StringProperty(required=True) # Bsp: Männlich
    expert = BooleanProperty(required=True) #Bsp: Ja / Nein
    # TODO: change to DateProperty
    activation_date = StringProperty(required=True)
    # local_association = StringProperty(required=True)

    # Relationships
    # skill = RelationshipTo("Qualification", "has")
    # regional_area = RelationshipTo("RegionalArea", "works_in")
    # federal_state = RelationshipTo("FederalState", "works_in")
    # city =  RelationshipTo("City", "works_in")
    lives_at = Relationship(".location.Location", "t_lives_at")
    has_qualification = Relationship(".qualifications.Qualifications", "t_has_qualification")
    assigned_to = Relationship(".unit.Unit", "i_assigned_to")
    executes = Relationship(".function.Function", "i_executes")
