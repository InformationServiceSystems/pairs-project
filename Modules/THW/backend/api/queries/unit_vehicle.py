from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.vehicle import Vehicle
from statistics import mean, stdev

def unit_vehicle(name):
    query = f'''
    MATCH
    (unit:Unit {{
        name: "{name}"}})
    - [r1:t_drives] -
    (vehicle:Vehicle)
    RETURN DISTINCT(vehicle)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    vehicles = [e[0] for e in results]
    vehicles = [{
        "name": e.name,
        } for e in vehicles]

    return {"data": vehicles} 
