
from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.function import Function
from statistics import mean, stdev

def unit_function(name):
    query = f'''
    MATCH
    (unit:Unit {{
        name: "{name}"}})
    - [r1:t_composed_of] -
    (function:Function)
    RETURN DISTINCT(function)
    UNION
    MATCH
    (unit:Unit WHERE unit.name =~ "(?i).*{name}.*")
    - [r1:t_composed_of] -
    (function:Function)
    RETURN DISTINCT(function)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)


    if len(results) == 0:
        return {}

    function = [e[0] for e in results]
    function = [{
        "name": e.name,
        "number": e.number
        } for e in function]

    return {"data": function} 
