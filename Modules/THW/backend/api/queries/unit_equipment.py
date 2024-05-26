from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.equipment import Equipment
from statistics import mean, stdev

def unit_equipment(name):
    query = f'''
    MATCH
    (unit:Unit {{
        name: "{name}"}})
    - [r1:t_uses] -
    (equipment:Equipment)
    RETURN DISTINCT(equipment)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)


    if len(results) == 0:
        return {}

    equipments = [e[0] for e in results]
    equipments = [{
        "name": e.name,
        "number": e.number
        } for e in equipments]

    return {"data": equipments} 
