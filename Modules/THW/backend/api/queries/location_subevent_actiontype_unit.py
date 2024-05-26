from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.unit import Unit
from statistics import mean, stdev

def location_subevent_actiontype_unit(location_city, subevent_name, actiontype_name):
    action_category = "kern";
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
    (action:Action WHERE action.category =~ "(?i).*$ACTION_CATEGORY.*")
    - [r5:s_consists_of] -
    (actiontype:ActionType WHERE actiontype.name =~ "(?i).*$ACTIONTYPE_NAME.*")
    WITH action
    MATCH (action) - [r6:t_fulfills] - (unit:Unit)
     RETURN DISTINCT(unit)
    '''
    query = query.replace("$LOCATION_CITY", location_city)
    query = query.replace("$SUBEVENT_NAME", subevent_name)
    query = query.replace("$ACTION_CATEGORY", action_category)
    query = query.replace("$ACTIONTYPE_NAME", actiontype_name)

    print(query)

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    units = [e[0] for e in results]
    units = [{"name": e.name,
              "description": e.description,
              "strength": e.strength,
              "abbreviation": e.abbreviation} for e in units]

    return {"data": units}

if __name__ == "__main__":
    pprint(location_subevent_actiontype_unit("ahrweiler", "hochwasser", ""))

