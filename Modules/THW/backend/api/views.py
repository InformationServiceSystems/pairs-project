from django.http import JsonResponse

from .queries.location_subevent_actiontype_unit import location_subevent_actiontype_unit
from .queries.location_subevent_actor import location_subevent_actor
from .queries.location_subevent_impact import location_subevent_impact
from .queries.subevent_event import subevent_event
from .queries.location import location
from .queries.subevent import subevent
from .queries.actiontype import actiontype
from .queries.unit_equipment import unit_equipment
from .queries.unit_function import unit_function
from .queries.unit_vehicle import unit_vehicle
from .queries.function_qualification import function_qualification
from .queries.qualification_person import qualification_person

from .queries.location_subevent_actiontype_action import location_subevent_actiontype_action
from .queries.action_subtask import action_subtask


def query_locations(request):
    data = location()
    return JsonResponse(data) 

def query_subevents(request):
    data = subevent()
    return JsonResponse(data) 

def query_action_types(request):
    data = actiontype()
    return JsonResponse(data) 

def query_subevent_event(request):
    subevent_name = request.GET.get("subevent_name")
    if not subevent_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'subevent_name'"
            })
    data = subevent_event(subevent_name)
    return JsonResponse(data) 

def query_location_subevent_impact(request):
    location_city = request.GET.get("location_city")
    subevent_name = request.GET.get("subevent_name")
    if not subevent_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'subevent_name'"
            })
    if not location_city:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'location_city'"
            })
    data = location_subevent_impact(location_city, subevent_name)
    return JsonResponse(data) 

def query_location_subevent_actor(request):
    location_city = request.GET.get("location_city")
    subevent_name = request.GET.get("subevent_name")
    if not subevent_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'subevent_name'"
            })
    if not location_city:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'location_city'"
            })
    data = location_subevent_actor(location_city, subevent_name)
    return JsonResponse(data) 

def query_location_subevent_actiontype_unit(request):
    location_city = request.GET.get("location_city")
    subevent_name = request.GET.get("subevent_name")
    actiontype_name = request.GET.get("actiontype_name")
    if not subevent_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'subevent_name'"
            })
    if not location_city:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'location_city'"
            })
    if not actiontype_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'actiontype_name'"
            })
    data = location_subevent_actiontype_unit(location_city, subevent_name, actiontype_name)
    return JsonResponse(data) 

def query_unit_equipment(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = unit_equipment(name)
    return JsonResponse(data) 

def query_unit_function(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = unit_function(name)
    return JsonResponse(data) 

def query_unit_vehicle(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = unit_vehicle(name)
    return JsonResponse(data) 

def query_function_qualification(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = function_qualification(name)
    return JsonResponse(data) 

def query_qualification_person(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = qualification_person(name)
    return JsonResponse(data) 

def query_action_subtask(request):
    name = request.GET.get("name")
    if not name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'name'"
            })
    data = action_subtask(name)
    return JsonResponse(data) 

def query_location_subevent_actiontype_action(request):
    location_city = request.GET.get("location_city")
    subevent_name = request.GET.get("subevent_name")
    actiontype_name = request.GET.get("actiontype_name")
    if not subevent_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'subevent_name'"
            })
    if not location_city:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'location_city'"
            })
    if not actiontype_name:
        return JsonResponse({
                "status": "ui-error",
                "message": f"missing argument 'actiontype_name'"
            })
    data = location_subevent_actiontype_action(location_city, subevent_name, actiontype_name)
    return JsonResponse(data) 
