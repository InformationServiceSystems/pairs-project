from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.event import Event
from statistics import mean, stdev

def subevent_event(subevent_name):
    query = '''
    MATCH
    (s:Subevent WHERE s.name =~ "(?i).*$SUBEVENT_NAME.*")
    - [:s_belongs_to] -
    (e:Event)
    return distinct(e)
    '''
    query = query.replace("$SUBEVENT_NAME", subevent_name)

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    events = [e[0] for e in results]
    events = [{"name": e.name,
               "hazard_type": e.hazard_type} for e in events]

    return {"data": events}


if __name__ == "__main__":
    pprint(query_subevent_event("regen"))

