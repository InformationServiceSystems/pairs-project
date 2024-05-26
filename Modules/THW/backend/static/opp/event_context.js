function updateEventContextEvent(subevent_name) {
    var data = querySubeventEvent(subevent_name);

    var name = $("#event_context-eventName");
    var hazardType = $("#event_context-eventHazardType");
    name.empty();
    hazardType.empty();

    data.then(function (data) {
        if (!("data" in data) || !(data["data"])) {
            name.append(noData());
            hazardType.append(noData());
            return;
        }
        data = data["data"][0];
        name.text(data["name"]);
        hazardType.text(data["hazard_type"]);
    });
}

function updateEventContextImpact(location_city, subevent_name) {
    var data = queryLocationSubeventImpact(location_city, subevent_name);

    var mean = $("#event_context-impactMean");
    var stdev= $("#event_context-impactStdev");
    mean.empty();
    stdev.empty();
    data.then(function (data) {
        if (!("data" in data) || !(data["data"])) {
            mean.append(noData());
            stdev.append(noData());
            return;
        }
        data = data["data"];
        mean.text( data["mean"] + " (dd:hh:mm:ss)");
        stdev.text("max. historical variance: " + data["variance"] + " (dd:hh:mm:ss)");
    });
}

function updateEventContextActor(location_city, subevent_name) {
    var data = queryLocationSubeventActor(location_city, subevent_name);

    var mean = $("#event_context-actorMean");
    var stdev= $("#event_context-actorStdev");
    var meanHelpers = $("#event_context-actorMeanHelpers");
    mean.empty();
    stdev.empty();
    meanHelpers.empty();

    data.then(function (data) {
        if (!("data" in data) || !(data["data"])) {
            mean.append(noData());
            stdev.append(noData());
            meanHelpers.append(noData());
            return;
        }
        data = data["data"];
        mean.text(data["mean_duty_hours"]);
        stdev.text("max. historical variance: " + data["stdev_duty_hours"]);
        meanHelpers.text(data["mean_number_helpers"]);
    });
}

function updateEventContext() {
    var subevent_name = getSelectedSubevent();
    var location_city = getSelectedCity();

    updateEventContextEvent(subevent_name);
    updateEventContextActor(location_city, subevent_name);
    updateEventContextImpact(location_city, subevent_name);
}


$(function () {

});
