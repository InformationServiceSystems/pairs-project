from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.person import Person
from statistics import mean, stdev

def qualification_person(name):
    query = f'''
    MATCH
    (qualifications:Qualifications {{
        name: "{name}"}})
    - [r1:t_has_qualification] -
    (person:Person)
    RETURN DISTINCT(person)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    persons = [e[0] for e in results]
    persons = [{
        "age": e.age,
        "gender": e.gender,
        "expert": e.expert,
        "activation_date": e.activation_date} for e in persons]

    return {"data": persons} 
