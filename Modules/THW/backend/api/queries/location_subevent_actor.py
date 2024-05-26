from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.actor import Actors
from statistics import mean, stdev

def location_subevent_actor(location_city, subevent_name):
    query = '''
    MATCH
    (location:Location WHERE location.city =~ "(?i).*$LOCATION_CITY.*") 
    - [r1:t_happens_at] - 
    (sp:ScenarioPattern) 
    - [r2:t_identified_by] -
    (s:Subevent WHERE s.name =~ "(?i).*$SUBEVENT_NAME.*")
    WITH sp
    MATCH (sp) - [:t_involves] - (i:Actors)
    RETURN distinct(i)
    '''
    query = query.replace("$LOCATION_CITY", location_city)
    query = query.replace("$SUBEVENT_NAME", subevent_name)

    print(query)

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    actors = [e[0] for e in results]

    mean_duty_hours = round(mean([a.duty_hours for a in actors]))
    stdev_duty_hours = 0 if len(actors) < 2 else round(stdev([a.duty_hours for a in actors]))
    mean_number_helpers = round(mean([a.number_of_helpers for a in actors]))

    return {"data": {"mean_duty_hours": mean_duty_hours,
            "stdev_duty_hours": stdev_duty_hours,
            "mean_number_helpers": mean_number_helpers}}


if __name__ == "__main__":
    pprint(location_subevent_actor("amberg", "hochwasser"))

