from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.actiontype import ActionType
from statistics import mean, stdev

def actiontype():
    query = '''
    MATCH
    (m:ActionType)
    return distinct(m.name)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    actiontypes = [e[0] for e in results]

    return {"data": actiontypes}


if __name__ == "__main__":
    pprint(location())


