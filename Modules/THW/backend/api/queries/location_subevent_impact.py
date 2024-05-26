from neomodel import config
from neomodel import db
from pprint import pprint
config.DATABASE_URL = "bolt://neo4j:OperationsPlanning@localhost:7687"

from .nodes.impact import Impact
from statistics import mean, stdev

def location_subevent_impact(location_city, subevent_name):
    query = '''
    MATCH
    (location:Location WHERE location.city =~ "(?i).*$LOCATION_CITY.*") 
    - [r1:t_happens_at] - 
    (sp:ScenarioPattern) 
    - [r2:t_identified_by] -
    (s:Subevent WHERE s.name =~ "(?i).*$SUBEVENT_NAME.*")
    WITH sp
    MATCH (sp) - [:t_creates] - (i:Impact)
    RETURN distinct(i)
    '''
    query = query.replace("$LOCATION_CITY", location_city)
    query = query.replace("$SUBEVENT_NAME", subevent_name)
    print(query)

    results, meta  = db.cypher_query(query, resolve_objects = True)

    if len(results) == 0:
        return {}

    durations = [e[0].duration for e in results]
    fixed_durations = [process_duration(duration) for duration in durations]
    average_duration = seconds_to_duration(mean([duration_to_seconds(duration) for duration in  fixed_durations]))
    variance_duration = 0 if len(durations) < 2 else seconds_to_duration(stdev([duration_to_seconds(duration) for duration in  fixed_durations]))

    # pprint(durations)
    # print(f"Mean: {average_duration}")
    # print(f"Variance: {variance_duration}")
    return {"data": {"mean": average_duration,
                     "variance": variance_duration}}
        

def process_duration(duration_str):
    parts = duration_str.split(",")
    if len(parts) == 1:
        return duration_str
    elif len(parts) == 2 and "day" in parts[0]:
        days = parts[0].split(" ")[0]
        return f"{days}:{parts[1].strip()}"
    return "Error"


def duration_to_seconds(duration):
    parts = duration.split(":")
    parts.reverse()
    seconds = 0
    for i, part in enumerate(parts):
        if i == 0:
            multiplier = 1
        elif i == 1:
            multiplier = 60
        elif i == 2:
            multiplier = 60*60
        elif i == 3:
            multiplier = 60*60*24
        seconds += int(part) * multiplier
    return seconds


def seconds_to_duration(seconds):
    seconds = int(seconds)
    days = 60*60*24
    hours = 60*60
    minutes = 60
    duration = []

    calculated_days = seconds // days
    duration.append(str(calculated_days))
    seconds = seconds % days

    calculated_hours = seconds // hours
    duration.append(str(calculated_hours))
    seconds = seconds % hours

    calculated_minutes = seconds // minutes
    duration.append(str(calculated_minutes))
    seconds = seconds % minutes

    calculated_seconds = seconds
    duration.append(str(calculated_seconds))

    duration_str = f"{calculated_days:02d}:{calculated_hours:02d}:{calculated_minutes:02d}:{calculated_seconds:02d}"
    return duration_str


if __name__ == "__main__":
    pprint(location_subevent_impact("amberg", "sonstige"))

