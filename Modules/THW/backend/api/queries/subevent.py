from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.subevent import Subevent
from statistics import mean, stdev

def subevent():
    query = '''
    MATCH
    (m:Subevent)
    return distinct(m.name)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    subevents = [e[0] for e in results]

    return {"data": subevents}


if __name__ == "__main__":
    pprint(subevent())


