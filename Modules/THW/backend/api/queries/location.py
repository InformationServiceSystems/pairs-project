from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.location import Location
from statistics import mean, stdev

def location():
    query = '''
    MATCH
    (m:Location)
    return distinct(m.city)
    '''

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    locations = [e[0] for e in results]

    return {"data": locations}


if __name__ == "__main__":
    pprint(location())


