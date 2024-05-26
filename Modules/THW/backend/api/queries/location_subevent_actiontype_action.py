from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.action import Action
from statistics import mean, stdev

def location_subevent_actiontype_action(location_city, subevent_name, actiontype_name):
    query = '''
        MATCH
    (location:Location WHERE location.city =~  "(?i).*$LOCATION_CITY.*") 
    - [r1:t_happens_at] - 
    (sp:ScenarioPattern) 
    - [r2:t_identified_by] -
    (subevent:Subevent WHERE subevent.name =~ "(?i).*$SUBEVENT_NAME.*")
    - [r3:t_has_subtask] -
    (subtask:Subtask)
    - [r4:s_subordinated] -
    (action:Action)
    - [r5:s_consists_of] -
    (actiontype:ActionType WHERE actiontype.name =~ "(?i).*$ACTIONTYPE_NAME.*")
     RETURN DISTINCT(action)
    '''
    query = query.replace("$LOCATION_CITY", location_city)
    query = query.replace("$SUBEVENT_NAME", subevent_name)
    query = query.replace("$ACTIONTYPE_NAME", actiontype_name)

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    actions = [e[0] for e in results]
    actions = [{"name": e.name,
               "description": e.description,
               "category": e.category} for e in actions]

    return {"data": actions}
