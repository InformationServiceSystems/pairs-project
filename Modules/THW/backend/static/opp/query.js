function noData() {
    //return $(`
        //<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar2-x-fill" viewBox="0 0 16 16">
            //<path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5m9.954 3H2.545c-.3 0-.545.224-.545.5v1c0 .276.244.5.545.5h10.91c.3 0 .545-.224.545-.5v-1c0-.276-.244-.5-.546-.5m-6.6 5.146a.5.5 0 1 0-.708.708L7.293 10l-1.147 1.146a.5.5 0 0 0 .708.708L8 10.707l1.146 1.147a.5.5 0 0 0 .708-.708L8.707 10l1.147-1.146a.5.5 0 0 0-.708-.708L8 9.293z"/>
        //</svg>
    //`);
    return "No datapoints available..."
}

function loading() {
    return $(`
        <div class="spinner-border" role="status"></div>
        `);
}

function getLocations() {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-locations";
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function getEvents() {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-subevents";
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function getActionTypes() {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-actiontypes";
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function querySubeventEvent(subevent_name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-subevent-event";
    url += "?subevent_name=" + subevent_name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryLocationSubeventImpact(location_city, subevent_name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-location-subevent-impact";
    url += "?location_city=" + location_city;
    url += "&subevent_name=" + subevent_name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryLocationSubeventActor(location_city, subevent_name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-location-subevent-actor";
    url += "?location_city=" + location_city;
    url += "&subevent_name=" + subevent_name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryLocationSubeventActiontypeUnit(location_city, subevent_name, actiontype_name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-location-subevent-actiontype-unit";
    url += "?location_city=" + location_city;
    url += "&subevent_name=" + subevent_name;
    url += "&actiontype_name=" + actiontype_name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryUnitEquipment(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-unit-equipment";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryUnitFunction(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-unit-function";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryUnitVehicle(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-unit-vehicle";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryFunctionQualification(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-function-qualification";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryQualificationPerson(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-qualification-person";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryActionSubtask(name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-action-subtask";
    url += "?name=" + name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function queryLocationSubeventActiontypeAction(location_city, subevent_name, actiontype_name) {
    var url = document.location.protocol + "//" + document.location.host;
    url += "/api/query-location-subevent-actiontype-action";
    url += "?location_city=" + location_city;
    url += "&subevent_name=" + subevent_name;
    url += "&actiontype_name=" + actiontype_name;
    return Promise.resolve($.ajax({
        dataType: "json",
        url: url,
        type: "GET",
    }));
}

function echo(message) {
    return ">> " + message;
}
