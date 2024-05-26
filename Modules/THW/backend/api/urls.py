from django.urls import path

from .views import query_locations
from .views import query_subevents
from .views import query_action_types
from .views import query_subevent_event
from .views import query_location_subevent_impact 
from .views import query_location_subevent_actor
from .views import query_location_subevent_actiontype_unit 
from .views import query_unit_equipment
from .views import query_unit_function
from .views import query_unit_vehicle
from .views import query_function_qualification
from .views import query_qualification_person
from .views import query_location_subevent_actiontype_action
from .views import query_action_subtask

urlpatterns = [
    path("query-locations", query_locations, name="query_locations"),
    path("query-subevents", query_subevents, name="query_subevents"),
    path("query-actiontypes", query_action_types, name="query_action_types"),
    path("query-subevent-event", query_subevent_event, name="query_subevent_event"),
    path("query-location-subevent-impact", query_location_subevent_impact, name="query_location_subevent_impact"),
    path("query-location-subevent-actor", query_location_subevent_actor, name="query_location_subevent_actor"),
    path("query-location-subevent-actiontype-unit", query_location_subevent_actiontype_unit, name="query_location_subevent_actiontype_unit"),
    path("query-unit-equipment", query_unit_equipment, name="query_unit_equipment"),
    path("query-unit-function", query_unit_function, name="query_unit_function"),
    path("query-unit-vehicle", query_unit_vehicle, name="query_unit_vehicle"),
    path("query-function-qualification", query_function_qualification, name="query_function_qualification"),
    path("query-qualification-person", query_qualification_person, name="query_qualification_person"),
    path("query-action-subtask", query_action_subtask, name="query_action_subtask"),
    path("query-location-subevent-actiontype-action", query_location_subevent_actiontype_action, name="query_location_subevent_actiontype_action"),
]
