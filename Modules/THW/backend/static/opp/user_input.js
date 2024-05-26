function getSelectedSubevent() {
    return $("#eventList").val() || ".";
}

function getSelectedCity() {
    return $("#locationList").val() || ".";
}

function getSelectedActionType() {
    return $("#actionTypeList").val() || ".";
}

$(function () {

    function updateLocationListOptions() {
        // Fetch locations
        var locations = getLocations();
        locations.then(function (data) {
            // Delete previous list entries
            var id = "#locationListOptions";
            var list = $(id);
            list.empty();

            $.each(data["data"], function(i, item) {
                list.append($("<option>", {
                    value: item
                }));
            });
        });
    }

    function updateEventListOptions() {
        // Fetch events
        var events = getEvents();
        events.then(function (data) {
            // Delete previous list entries
            var id = "#eventListOptions";
            var list = $(id);
            list.empty();

            $.each(data["data"], function(i, item) {
                list.append($("<option>", {
                    value: item
                }));
            });
        });
    }

    function updateActionTypeListOptions() {
        // Fetch actionTypes
        var actionTypes = getActionTypes();
        actionTypes.then(function (data) {
            // Delete previous list entries
            var id = "#actionTypeListOptions";
            var list = $(id);
            list.empty();

            $.each(data["data"], function(i, item) {
                list.append($("<option>", {
                    value: item
                }));
            });
        });
    }

    function fetchResuts() {
        updateEventContext();
        updateUnits();
        updateActions();
        renderGraph();
    }

    function init() {
        updateLocationListOptions();
        updateEventListOptions();
        updateActionTypeListOptions();
        $("#fetchResults").click(fetchResuts);
    }

    init()

});
