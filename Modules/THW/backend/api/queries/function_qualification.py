from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.qualifications import Qualifications
from statistics import mean, stdev

def function_qualification(name):
    query = f'''
    MATCH
    (function:Function {{
        name: "{name}"}})
    - [r1] -
    (additionalFunction:AdditionalFunction)
    - [r2] -
    (qualifications:Qualifications)
    RETURN DISTINCT(qualifications)
    UNION
    MATCH
    (function:Function {{
        name: "{name}"}})
    - [r3] -
    (qualifications:Qualifications)
    RETURN DISTINCT(qualifications)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    qualifications = [e[0] for e in results]
    qualifications = [{
        "name": e.name,
        } for e in qualifications]


    return {"data": qualifications}
