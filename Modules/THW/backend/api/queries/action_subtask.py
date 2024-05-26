from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.subtask import Subtask
from statistics import mean, stdev

def action_subtask(name):
    query = f'''
    MATCH
    (action:Action {{
        name: "{name}"}})
    - [r1:s_subordinated] -
    (subtask:Subtask)
    RETURN DISTINCT(subtask)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)


    if len(results) == 0:
        return {}

    subtasks = [e[0] for e in results]
    subtasks = [{
        "name": e.name,
        } for e in subtasks]

    return {"data": subtasks} 
