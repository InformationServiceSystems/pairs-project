const selectEvent = document.getElementById('events-dropdown');
const selectAction = document.getElementById('actions-dropdown');
const selectCity = document.getElementById('city-dropdown-r');

var selectedEvent = '';
var selectedCity = '';
var selectedAction = '';

function updateUI(){
    console.log('updateUI');
    console.log(selectedEvent);
    console.log(selectedCity);

    const optionActions = selectAction.options;


    if(selectedEvent === 'Hochwasser' && selectedCity ===  "biberach"){
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Ortungs-, Rettungs-, Bergungsmaßnahmen") {
                optionActions[i].disabled = false;
            }else{
                optionActions[i].disabled = true;
            }
        }
    }else if(selectedEvent === 'Hochwasser' && selectedCity ===  "goettingen"){
        for (let i = 0; i < optionActions.length; i++) {
            if(optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen"){
                optionActions[i].disabled = false;
            }else{
                optionActions[i].disabled = true;
            }
        }

    }else if(selectedEvent === 'Starkregen'  && selectedCity ===  "goettingen"){
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Führung, Führungsunterstützung und Verbindung") {
                optionActions[i].disabled = false;
            }else{
                optionActions[i].disabled = true;
            }
        }
    }else if(selectedEvent === 'Starkregen'  && selectedCity ===  "biberach"){
        for (let i = 0; i < optionActions.length; i++) {
            if(optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen"){
                optionActions[i].disabled = false;
            }
            else{
                optionActions[i].disabled = true;
            }
        }
    }else if(selectedEvent == 'yyy'  && selectedCity ==  "xxx"){
        for (let i = 0; i < optionActions.length; i++) {
            if(optionActions[i].value == "zzz"){
                optionActions[i].disabled = false;
            }
            else{
                optionActions[i].disabled = true;
            }
        }
    }else if (selectedEvent === 'Hochwasser' && selectedCity === "muelheim") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen"
          || optionActions[i].value === "Ortungs-, Rettungs-, Bergungsmaßnahmen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    }else if (selectedEvent === 'Hochwasser' && selectedCity === "zell") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }

    } else if (selectedEvent === 'Hochwasser' && selectedCity === "bernkastel_kues") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen"
                || optionActions[i].value === "Ortungs-, Rettungs-, Bergungsmaßnahmen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    }else if (selectedEvent === 'Hochwasser' && selectedCity === "cochem") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    } else if (selectedEvent === 'Hochwasser' && selectedCity === "bengel") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    } else if (selectedEvent === 'Starkregen' && selectedCity === "zell") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    } else if (selectedEvent === 'Starkregen' && selectedCity === "bengel") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    } else if (selectedEvent === 'Starkregen' && selectedCity === "cochem") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    }  else if (selectedEvent === 'Starkregen' && selectedCity === "bernkastel_kues") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen"
                || optionActions[i].value === "Führung, Führungsunterstützung und Verbindung") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    }else if (selectedEvent === 'Starkregen' && selectedCity === "muelheim") {
        for (let i = 0; i < optionActions.length; i++) {
            if (optionActions[i].value === "Bekämpfung von Überschwemmungen/Überflutungen") {
                optionActions[i].disabled = false;
            } else {
                optionActions[i].disabled = true;
            }
        }
    }else {
        console.log(selectedEvent);
        console.log(selectedCity);
    }
}

selectCity.addEventListener('change', function(event) {
    selectedCity = selectCity.value;
    if(selectedEvent !=''&& selectedCity != ''){
        updateUI()
    }

    //reset Action
    selectAction.selectedIndex = 0;

});

selectEvent.addEventListener('change', function(event) {
    selectedEvent = selectEvent.value;
    if(selectedEvent !='' && selectedCity != '' ){
        updateUI()
    }

    //reset Action
    selectAction.selectedIndex = 0;

});

//next script

var isButtonClicked = false;

function generateView(event){
    event.preventDefault();  // Prevent the default form submission behavior

    var table_btn_json = $('#button_op_json');
    var table_btn_table = $('#button_op_table');

    const jsonRenderer = $("#json-renderer");
    const jsonContainer = $(".json-container")[0];

    const warningTextJson = $("#warning_text_json");
    const warningText2 = $("#warning_text2");

    if (!isButtonClicked) {

        warningText2.css("display", "none");
        warningTextJson.css("display", "none");
        isButtonClicked = true;
        table_btn_json.css("display", "inline");
        table_btn_table.css("display", "inline");
        $(jsonContainer).css("overflowY", "scroll");
    }

    //btn
    const showButton = $("#generate_btn");

    //What event is chosen?
    const dropdown_event = $("#events-dropdown");
    const selectedOption_event = dropdown_event.find("option:selected");
    const selectedText_event = selectedOption_event.text();

    //What action is chosen?
    const dropdown_action = $("#actions-dropdown")
    const selectedOption_action = dropdown_action.find("option:selected");
    const selectedText_action = selectedOption_action.text();

    //What city is chosen?
    const dropdown_city = $("#city-dropdown-r")
    const selectedOption_city = dropdown_city.find("option:selected");
    const selectedText_city = selectedOption_city.text();



    const recommend_graph = $("#graph-container2");

    if(selectedText_event === 'Hochwasser'){
        recommend_graph.css("display","block");
    }

    const jsonFloodBek = document.getElementById("json-data-flood-bek");
    const jsonStarkregenF = document.getElementById("json-data-starkregen-fuehr");
    const jsonFloodOrd = document.getElementById("json-data-flood-ord");
    const jsonStarkregenBek = document.getElementById("json-data-starkregen-bek");

    //Filter JSON
    var jsonData ={};
/*    if (selectedText_event === 'Hochwasser' && selectedText_action === 'Ortungs-, Rettungs-, Bergungsmaßnahmen') {
        jsonData = JSON.parse(jsonFloodOrd.innerHTML);
    } else if (selectedText_event === 'Starkregen' && selectedText_action === 'Führung, Führungsunterstützung und Verbindung') {
        jsonData = JSON.parse(jsonStarkregenF.innerHTML);
    }else if (selectedText_event === 'Hochwasser' && selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen') {
        jsonData = JSON.parse(jsonFloodBek.innerHTML);*/

    if (selectedText_event === 'YYY' &&
        selectedText_action === 'ZZZ' &&
        selectedText_city === 'XXX') {
            jsonData = loadXXX_YYY_ZZZ();

    }else if (selectedText_event === 'YYY' &&
              selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
              selectedText_city === 'AAA') {
            jsonData = loadAAA_YYY();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Mülheim (Rheinland-Pfalz)') {
        jsonData = loadFMUb();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Ortungs-, Rettungs-, Bergungsmaßnahmen' &&
        selectedText_city === 'Mülheim (Rheinland-Pfalz)') {
        jsonData = loadFMO();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Zell (Rheinland-Pfalz)') {
        jsonData = loadFZUb();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Ortungs-, Rettungs-, Bergungsmaßnahmen' &&
        selectedText_city === 'Bernkastel-Kues (Rheinland-Pfalz)') {
        jsonData = loadFBernO();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Bernkastel-Kues (Rheinland-Pfalz)') {
        jsonData = loadFBernUb();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Führung, Führungsunterstützung und Verbindung' &&
        selectedText_city === 'Bernkastel-Kues (Rheinland-Pfalz)') {
        jsonData = loadRBernFue();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Bernkastel-Kues (Rheinland-Pfalz)') {
        jsonData = loadRBernUb();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Cochem (Rheinland-Pfalz)') {
        jsonData = loadFCUb();
    }
    else if (selectedText_event === 'Hochwasser' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Bengel (Rheinland-Pfalz)') {
        jsonData = loadFBUb();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Bengel (Rheinland-Pfalz)') {
        jsonData = loadRBUb();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Cochem (Rheinland-Pfalz)') {
        jsonData = loadRCUb();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Mülheim (Rheinland-Pfalz)') {
        jsonData = loadRMUb();
    }
    else if (selectedText_event === 'Starkregen' &&
        selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen' &&
        selectedText_city === 'Zell (Rheinland-Pfalz)') {
        jsonData = loadRZUb();
    }

    //PuT filtered JSON in HTML
    jsonRenderer.text(JSON.stringify(jsonData, null, 4));

    //CLICK EVENT when Table
    table_btn_table.on('click', function(event) {
        //Hide JSON
        jsonRenderer.css("display", "none");
        //Show Table view
        var operation_plan_div = $('#table_operation_plan')
        createTableView(jsonData, operation_plan_div);
        operation_plan_div.css("display","block");
    });

    //CLICK EVENT when JSON
    table_btn_json.on('click', function(event) {
        //Hide table view
        var operation_plan_div = $('#table_operation_plan');
        operation_plan_div.css("display","none");
        //Show JSON
        jsonRenderer.css("display", "block");
        $(jsonContainer).css("overflowY", "scroll");
    });


    //Build GRAPH
    buildRecommendation()
    // Simulate a click event
    table_btn_table.trigger('click');

    function createTableView(jsonData, operation_plan_div){
        //Clean from Old data
        operation_plan_div.empty();

        // Create the table element
        var table_overview = $('<table>').addClass('operation-plan-table').css('margin', '10px 5px').css('position','relative').css('top','10px').css('width','99%');
            // Create table rows for TotalNumberOfHelpers and workHours
            var reason = $('<tr>');
            reason.append($('<th>').text('Event'));
            reason.append($('<td>').text(jsonData.scenarioPattern[0]['pairs:Reason']['pairs:Precondition']));
            table_overview.append(reason);

            var totalDuration = $('<tr>');
            totalDuration.append($('<th>').text('Duration'));
            totalDuration.append($('<td>').text(jsonData.scenarioPattern[0]['pairs:Impact']['schema:Duration']));
            table_overview.append(totalDuration);

            var totalHelpersRow = $('<tr>');
            totalHelpersRow.append($('<th>').text('Total Number of Helpers'));
            totalHelpersRow.append($('<td>').text(jsonData.scenarioPattern[0]['foaf:Agent']['pairs:TotalNumberOfHelpers']));
            table_overview.append(totalHelpersRow);

            var workHoursRow = $('<tr>');
            workHoursRow.append($('<th>').text('Work Hours'));
            workHoursRow.append($('<td>').text(jsonData.scenarioPattern[0]['foaf:Agent']['schema:workHours']));
            table_overview.append(workHoursRow);


        //

        //222222222222222222222

        // Create the table element

        var responder_array = jsonData.scenarioPattern[0]['foaf:Agent']['beAware:Responder']

        for(var i=0;i<responder_array.length;i++){
            var unit_title = $('<div>').addClass('responder-table'+i).css('margin', '20px auto').css('text-align', 'center' ).css('font-weight', '700');
            var title_num = i+1
            unit_title.text('Unit ' + title_num);

            var table_responder = $('<table>').addClass('responder-table'+i).css('margin', '10px 5px').css('width','99%');

            var unitName = $('<tr>');
            unitName.append($('<th>').text('Unit Name'));
            unitName.append($('<td>').text(responder_array[i]['pairs:UnitName']));
            table_responder.append(unitName);

            var unitDescription = $('<tr>');
            unitDescription.append($('<th>').text('Unit Description'));
            unitDescription.append($('<td>').text(responder_array[i]['pairs:UnitDescription']));
            table_responder.append(unitDescription);

            var unitStrength = $('<tr>');
            unitStrength.append($('<th>').text('Unit Strength'));
            unitStrength.append($('<td>').text(responder_array[i]['pairs:UnitStrength']));
            table_responder.append(unitStrength);

            //ROLE-------------
            var table_role = $('<table>').addClass('responder-table-role'+i).css('margin', '10px 5px').css('width','99%');

            //Content
            var role = $('<tr>');
            role.append($('<th>').text('Role Name'));
            role.append($('<th>').text('Number Of Actors'));
            role.append($('<th>').text('Actor Function'));
            table_role.append(role);

            for(var j=0;j<responder_array[i]['pairs:Role'].length;j++){
                var role_j = $('<tr>');
                role_j.append($('<td>').text(responder_array[i]['pairs:Role'][j]['schema:name']));
                role_j.append($('<td>').text(responder_array[i]['pairs:Role'][j]['pairs:NumberOfActors']));
                role_j.append($('<td>').text(responder_array[i]['pairs:Role'][j]['pairs:ActorFunction']));
                table_role.append(role_j);
            }

            //Personal Table

            var personal_array = responder_array[i]['schema:Person']
            var table_personal = $('<table>').addClass('responder-table-personal-'+i).css('margin', '10px 5px').css('width','99%');

            //Caption Personal Table
            var personal_title = $('<div>').addClass('peronal-table-'+i).css('margin', '20px auto').css('text-align', 'center' ).css('font-weight', '700');
            personal_title.text('Personal ' + title_num);

            //Content
            var personal = $('<tr>');
            personal.append($('<th>').text('Id'));
            personal.append($('<th>').text('Gender'));
            personal.append($('<th>').text('Qualification'));
            table_personal.append(personal);

            for(var j=0;j<personal_array.length;j++){
                var role_j = $('<tr>');
                role_j.append($('<td>').text(personal_array[j]['@id']));
                role_j.append($('<td>').text(personal_array[j]['schema:gender']));
                role_j.append($('<td>').text(personal_array[j]['pairs:Qualification']));
                table_personal.append(role_j);
            }

            // Append the table to the operation_plan_div
            operation_plan_div.append(table_overview);
            operation_plan_div.append(unit_title);
            operation_plan_div.append(table_responder);
            operation_plan_div.append(table_role);
            operation_plan_div.append(personal_title);
            operation_plan_div.append(table_personal);

        }

        // ---------------RESOURCES ---------------
        var values_title = $('<div>').addClass('values-table').css('margin', '20px auto').css('text-align', 'center' ).css('font-weight', '700');
        values_title.text('Resources');
        operation_plan_div.append(values_title);

        var resources_all = jsonData.scenarioPattern[0]['pairs:Resource']
        var table_resource = $('<table>').addClass('responder-table-resource').css('margin', '10px 5px').css('width','99%');

        for (var key in resources_all) {
            if (resources_all.hasOwnProperty(key)) {

                var parts = key.split(':');

                if (parts.length > 1) {
                    var wordAfterColon = parts[1];
                    var capitalizedWord = wordAfterColon.charAt(0).toUpperCase() + wordAfterColon.slice(1);
                }

                var values = String(resources_all[key]);

                //Content
                if(key.length > 3){

                    var resource_i = $('<tr>');
                    resource_i.append($('<th style="font-weight: 400; width: 15%;">').text(capitalizedWord));
                    resource_i.append($('<th style="font-weight: 400;">').text(values));
                    table_resource.append(resource_i);

                    operation_plan_div.append(table_resource);
                }

            }
        }

    }
}

/*function loadJSONdata(filename){
    return
    $.ajax({
        url: filename,
        dataType: "json",
        success: function(response) {
            return response;
        }
    });

}*/

function loadXXX_YYY_ZZZ(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "67419",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "67419",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "67419",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "67419",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Bengel",\n' +
        '                      "schema:addressRegion": "Bengel (Mosel)",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                    "schema:addressLocality": "Bengel",\n' +
        '                    "schema:addressRegion": "Bengel (Mosel)",\n' +
        '                    "schema:State": "Rheinland-Pfalz",\n' +
        '                    "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "67419",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": ""\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "67419",\n' +
        '                "pairs:TotalNumberOfHelpers": "",\n' +
        '                "schema:workHours": "",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "1893",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1678",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7543",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1978",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1588",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1892",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "6782",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7839",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "9717",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7189",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8192",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8929",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8977",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "9202",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sanitätshelfer"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "10196",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  }\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "67419",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "67419",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')
}
function loadFMUb(){
    return JSON.parse('{\n' +
        '  "@context": [\n' +
        '    {\n' +
        '      "schema": "http://schema.org",\n' +
        '      "dct": "http://purl.org/dc/terms/",\n' +
        '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '      "pairs": "https://www.pairs-projekt.de/",\n' +
        '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '      "lode": "https://linkedevents.org/ontology/",\n' +
        '      "empathi": "https://w3id.org/empathi/1.0"\n' +
        '    }\n' +
        '  ],\n' +
        '  "scenarioPattern": [\n' +
        '    {\n' +
        '      "schema:identifier": {\n' +
        '        "@id": "917643",\n' +
        '        "schema:startDate": "14/11/2023",\n' +
        '        "schema:endDate": "15/11/2023"\n' +
        '      },\n' +
        '      "pairs:Context": {\n' +
        '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
        '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
        '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
        '        "schema:description": ""\n' +
        '      },\n' +
        '      "dct:Provenance": {\n' +
        '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '      },\n' +
        '      "schema:location": {\n' +
        '        "pairs:ReportLocation": {\n' +
        '          "schema:addressLocality": "Mülheim",\n' +
        '          "schema:addressRegion": "Mülheim",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        },\n' +
        '        "pairs:OperationLocation": {\n' +
        '          "schema:addressLocality": "Mülheim",\n' +
        '          "schema:addressRegion": "Mülheim",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        }\n' +
        '      },\n' +
        '      "pairs:Reason": {\n' +
        '        "pairs:Precondition": "Starkregen"\n' +
        '      },\n' +
        '      "pairs:Impact": {\n' +
        '        "pairs:Postcondition": "",\n' +
        '        "schema:Duration": ""\n' +
        '      },\n' +
        '      "foaf:Agent": {\n' +
        '        "pairs:TotalNumberOfHelpers": "",\n' +
        '        "schema:workHours": "",\n' +
        '        "beAware:Responder":[{\n' +
        '          "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '          "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '          "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '          "pairs:Role": [{\n' +
        '            "schema:name":"Gruppenführer/in",\n' +
        '            "pairs:NumberOfActors": "1",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Truppführer/in",\n' +
        '            "pairs:NumberOfActors": "2",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Fachhelfer/in",\n' +
        '            "pairs:NumberOfActors": "4",\n' +
        '            "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '          }],\n' +
        '          "schema:Person": [\n' +
        '          {\n' +
        '            "@id": "15773",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15889",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15443",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15992",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15998",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15994",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15772",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15441",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15765",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15432",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15555",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15667",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15429",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15879",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "15890",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sanitätshelfer"\n' +
        '          }\n' +
        '\n' +
        '          ]\n' +
        '        }]\n' +
        '      },\n' +
        '      "beAware:Mission": {\n' +
        '        "@id": "917643",\n' +
        '          "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '          "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '      },\n' +
        '      "pairs:Resource": {\n' +
        '        "@id": "917643",\n' +
        '          "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '        "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '      }\n' +
        '    }\n' +
        '  ]\n' +
        '}\n')}

function loadFBUb(){
    var x = JSON.parse('{\n' +
        '  "@context": [\n' +
        '    {\n' +
        '      "schema": "http://schema.org",\n' +
        '      "dct": "http://purl.org/dc/terms/",\n' +
        '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '      "pairs": "https://www.pairs-projekt.de/",\n' +
        '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '      "lode": "https://linkedevents.org/ontology/",\n' +
        '      "empathi": "https://w3id.org/empathi/1.0"\n' +
        '    }\n' +
        '  ],\n' +
        '  "scenarioPattern": [\n' +
        '    {\n' +
        '      "schema:identifier": {\n' +
        '        "@id": "789453",\n' +
        '        "schema:startDate": "",\n' +
        '        "schema:endDate": ""\n' +
        '      },\n' +
        '      "pairs:Context": {\n' +
        '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
        '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
        '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
        '        "schema:description": ""\n' +
        '      },\n' +
        '      "dct:Provenance": {\n' +
        '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '      },\n' +
        '      "schema:location": {\n' +
        '        "@id": "67419",\n' +
        '          "pairs:ReportLocation": {\n' +
        '              "schema:addressLocality": "Bengel",\n' +
        '              "schema:addressRegion": "Bengel (Mosel)",\n' +
        '              "schema:State": "Rheinland-Pfalz",\n' +
        '              "schema:addressCountry": "Germany"\n' +
        '          },\n' +
        '          "pairs:OperationLocation": {\n' +
        '            "schema:addressLocality": "Bengel",\n' +
        '            "schema:addressRegion": "Bengel (Mosel)",\n' +
        '            "schema:State": "Rheinland-Pfalz",\n' +
        '            "schema:addressCountry": "Germany"\n' +
        '          }\n' +
        '      },\n' +
        '      "pairs:Reason": {\n' +
        '        "pairs:Precondition": "Starkregen"\n' +
        '      },\n' +
        '      "pairs:Impact": {\n' +
        '        "pairs:Postcondition": "",\n' +
        '        "schema:Duration": ""\n' +
        '      },\n' +
        '      "foaf:Agent": {\n' +
        '        "pairs:TotalNumberOfHelpers": "",\n' +
        '        "schema:workHours": "",\n' +
        '        "beAware:Responder":[{\n' +
        '          "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '          "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '          "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '          "pairs:Role": [{\n' +
        '            "schema:name":"Gruppenführer/in",\n' +
        '            "pairs:NumberOfActors": "1",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Truppführer/in",\n' +
        '            "pairs:NumberOfActors": "2",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Fachhelfer/in",\n' +
        '            "pairs:NumberOfActors": "4",\n' +
        '            "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '          }],\n' +
        '          "schema:Person": [\n' +
        '          {\n' +
        '            "@id": "1893",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "1678",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "7543",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "1978",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "1588",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "1892",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "6782",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "7839",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "9717",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "7189",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "8192",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "8929",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "8977",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "9202",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sanitätshelfer"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "10196",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          }\n' +
        '          ]\n' +
        '        }]\n' +
        '      },\n' +
        '      "beAware:Mission": {\n' +
        '        "@id": "789453",\n' +
        '          "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '          "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '      },\n' +
        '      "pairs:Resource": {\n' +
        '        "@id": "789453",\n' +
        '          "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '        "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '      }\n' +
        '  }\n' +
        ']\n' +
        '}\n')
      return x}

function loadFZUb(){
    return JSON.parse('{\n' +
        '  "@context": [\n' +
        '    {\n' +
        '      "schema": "http://schema.org",\n' +
        '      "dct": "http://purl.org/dc/terms/",\n' +
        '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '      "pairs": "https://www.pairs-projekt.de/",\n' +
        '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '      "lode": "https://linkedevents.org/ontology/",\n' +
        '      "empathi": "https://w3id.org/empathi/1.0"\n' +
        '    }\n' +
        '  ],\n' +
        '  "scenarioPattern": [\n' +
        '    {\n' +
        '      "schema:identifier": {\n' +
        '        "@id": "789453",\n' +
        '        "schema:startDate": "14/11/2023",\n' +
        '        "schema:endDate": "15/11/2023"\n' +
        '      },\n' +
        '      "pairs:Context": {\n' +
        '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
        '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
        '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
        '        "schema:description": ""\n' +
        '      },\n' +
        '      "dct:Provenance": {\n' +
        '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '      },\n' +
        '      "schema:location": {\n' +
        '        "pairs:ReportLocation": {\n' +
        '            "schema:addressLocality": "Zell",\n' +
        '            "schema:addressRegion": "Trier",\n' +
        '            "schema:State": "Rheinland-Pfalz",\n' +
        '            "schema:addressCountry": "Germany"\n' +
        '        },\n' +
        '        "pairs:OperationLocation": {\n' +
        '            "schema:addressLocality": "Zell",\n' +
        '            "schema:addressRegion": "Trier",\n' +
        '            "schema:State": "Rheinland-Pfalz",\n' +
        '            "schema:addressCountry": "Germany"\n' +
        '        }\n' +
        '      },\n' +
        '      "pairs:Reason": {\n' +
        '        "pairs:Precondition": "Starkregen"\n' +
        '      },\n' +
        '      "pairs:Impact": {\n' +
        '        "pairs:Postcondition": "",\n' +
        '        "schema:Duration": "00:48:21:00"\n' +
        '      },\n' +
        '      "foaf:Agent": {\n' +
        '        "pairs:TotalNumberOfHelpers": "9",\n' +
        '        "schema:workHours": "290",\n' +
        '        "beAware:Responder":[{\n' +
        '          "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '          "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '          "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '          "pairs:Role": [{\n' +
        '            "schema:name":"Gruppenführer/in",\n' +
        '            "pairs:NumberOfActors": "1",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Truppführer/in",\n' +
        '            "pairs:NumberOfActors": "2",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Fachhelfer/in",\n' +
        '            "pairs:NumberOfActors": "4",\n' +
        '            "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '          }],\n' +
        '          "schema:Person": [\n' +
        '          {\n' +
        '            "@id": "3652",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3791",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3667",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3942",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3988",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3956",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3544",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "3462",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2784",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          }\n' +
        '          ]\n' +
        '        }]\n' +
        '      },\n' +
        '      "beAware:Mission": {\n' +
        '        "@id": "789453",\n' +
        '          "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '          "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '      },\n' +
        '      "pairs:Resource": {\n' +
        '        "@id": "789453",\n' +
        '          "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '        "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '      }\n' +
        '    }\n' +
        '  ]\n' +
        '}\n')}

function loadFCUb(){
    return JSON.parse('{\n' +
        '  "@context": [\n' +
        '    {\n' +
        '      "schema": "http://schema.org",\n' +
        '      "dct": "http://purl.org/dc/terms/",\n' +
        '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '      "pairs": "https://www.pairs-projekt.de/",\n' +
        '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '      "lode": "https://linkedevents.org/ontology/",\n' +
        '      "empathi": "https://w3id.org/empathi/1.0"\n' +
        '    }\n' +
        '  ],\n' +
        '  "scenarioPattern": [\n' +
        '    {\n' +
        '      "schema:identifier": {\n' +
        '        "@id": "789453",\n' +
        '        "schema:startDate": "14/11/2023",\n' +
        '        "schema:endDate": "15/11/2023"\n' +
        '      },\n' +
        '      "pairs:Context": {\n' +
        '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
        '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
        '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
        '        "schema:description": ""\n' +
        '      },\n' +
        '      "dct:Provenance": {\n' +
        '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '      },\n' +
        '      "schema:location": {\n' +
        '        "pairs:ReportLocation": {\n' +
        '          "schema:addressLocality": "Cochem",\n' +
        '          "schema:addressRegion": "Trier",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        },\n' +
        '        "pairs:OperationLocation": {\n' +
        '          "schema:addressLocality": "Cochem",\n' +
        '          "schema:addressRegion": "Trier",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        }\n' +
        '      },\n' +
        '      "pairs:Reason": {\n' +
        '        "pairs:Precondition": "Starkregen"\n' +
        '      },\n' +
        '      "pairs:Impact": {\n' +
        '        "pairs:Postcondition": "",\n' +
        '        "schema:Duration": "00:19:00:00"\n' +
        '      },\n' +
        '      "foaf:Agent": {\n' +
        '        "pairs:TotalNumberOfHelpers": "4",\n' +
        '        "schema:workHours": "73",\n' +
        '        "beAware:Responder":[{\n' +
        '          "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '          "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '          "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '          "pairs:Role": [{\n' +
        '            "schema:name":"Gruppenführer/in",\n' +
        '            "pairs:NumberOfActors": "1",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Truppführer/in",\n' +
        '            "pairs:NumberOfActors": "2",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Fachhelfer/in",\n' +
        '            "pairs:NumberOfActors": "4",\n' +
        '            "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '          }],\n' +
        '          "schema:Person": [\n' +
        '          {\n' +
        '            "@id": "16787",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "16566",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "16321",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "16432",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          }\n' +
        '          ]\n' +
        '        }]\n' +
        '      },\n' +
        '      "beAware:Mission": {\n' +
        '        "@id": "789453",\n' +
        '          "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '          "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '      },\n' +
        '      "pairs:Resource": {\n' +
        '        "@id": "789453",\n' +
        '          "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '        "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '      }\n' +
        '  }\n' +
        ']\n' +
        '}\n')}

function loadFBernUb(){
    return JSON.parse('{\n' +
        '  "@context": [\n' +
        '    {\n' +
        '      "schema": "http://schema.org",\n' +
        '      "dct": "http://purl.org/dc/terms/",\n' +
        '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '      "pairs": "https://www.pairs-projekt.de/",\n' +
        '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '      "lode": "https://linkedevents.org/ontology/",\n' +
        '      "empathi": "https://w3id.org/empathi/1.0"\n' +
        '    }\n' +
        '  ],\n' +
        '  "scenarioPattern": [\n' +
        '    {\n' +
        '      "schema:identifier": {\n' +
        '        "@id": "789453",\n' +
        '        "schema:startDate": "14/11/2023",\n' +
        '        "schema:endDate": "15/11/2023"\n' +
        '      },\n' +
        '      "pairs:Context": {\n' +
        '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
        '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
        '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
        '        "schema:description": ""\n' +
        '      },\n' +
        '      "dct:Provenance": {\n' +
        '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '      },\n' +
        '      "schema:location": {\n' +
        '        "pairs:ReportLocation": {\n' +
        '          "schema:addressLocality": "Bernkastel-Kues",\n' +
        '          "schema:addressRegion": "Wittlich",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        },\n' +
        '        "pairs:OperationLocation": {\n' +
        '          "schema:addressLocality": "Bernkastel-Kues",\n' +
        '          "schema:addressRegion": "Wittlich",\n' +
        '          "schema:State": "Rheinland-Pfalz",\n' +
        '          "schema:addressCountry": "Germany"\n' +
        '        }\n' +
        '      },\n' +
        '      "pairs:Reason": {\n' +
        '        "pairs:Precondition": "Starkregen"\n' +
        '      },\n' +
        '      "pairs:Impact": {\n' +
        '        "pairs:Postcondition": "",\n' +
        '        "schema:Duration": "00:17:00:00"\n' +
        '      },\n' +
        '      "foaf:Agent": {\n' +
        '        "pairs:TotalNumberOfHelpers": "13",\n' +
        '        "schema:workHours": "236",\n' +
        '        "beAware:Responder":[{\n' +
        '          "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '          "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '          "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '          "pairs:Role": [{\n' +
        '            "schema:name":"Gruppenführer/in",\n' +
        '            "pairs:NumberOfActors": "1",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Truppführer/in",\n' +
        '            "pairs:NumberOfActors": "2",\n' +
        '            "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '          },\n' +
        '          {\n' +
        '            "schema:name":"Fachhelfer/in",\n' +
        '            "pairs:NumberOfActors": "4",\n' +
        '            "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '          }],\n' +
        '          "schema:Person": [\n' +
        '          {\n' +
        '            "@id": "2763",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2799",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2578",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2542",\n' +
        '            "schema:gender": "Weiblich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2679",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2655",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2654",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2998",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2699",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          },\n' +
        '          {\n' +
        '            "@id": "2678",\n' +
        '            "schema:gender": "Männlich",\n' +
        '            "pairs:Qualification": "Grundausbildung"\n' +
        '          }\n' +
        '          ]\n' +
        '        }]\n' +
        '      },\n' +
        '      "beAware:Mission": {\n' +
        '        "@id": "789453",\n' +
        '          "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '          "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '      },\n' +
        '      "pairs:Resource": {\n' +
        '        "@id": "789453",\n' +
        '          "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '        "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '      }\n' +
        '  }\n' +
        ']\n' +
        '}\n')}

function loadRMUb(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "298763",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "5631560",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "298763",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "298763",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Mülheim",\n' +
        '                      "schema:addressRegion": "Mülheim",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                      "schema:addressLocality": "Mülheim",\n' +
        '                      "schema:addressRegion": "Mülheim",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "298763",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": ""\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "298763",\n' +
        '                "pairs:TotalNumberOfHelpers": "",\n' +
        '                "schema:workHours": "",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "15773",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15889",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15443",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15992",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15998",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15994",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15772",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15441",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15765",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15432",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15555",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15667",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15429",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15879",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "15890",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sanitätshelfer"\n' +
        '                  }\n' +
        '\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "298763",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "298763",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')}

function loadRBUb(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "67419",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "67419",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "67419",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "67419",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Bengel",\n' +
        '                      "schema:addressRegion": "Bengel (Mosel)",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                    "schema:addressLocality": "Bengel",\n' +
        '                    "schema:addressRegion": "Bengel (Mosel)",\n' +
        '                    "schema:State": "Rheinland-Pfalz",\n' +
        '                    "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "67419",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": ""\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "67419",\n' +
        '                "pairs:TotalNumberOfHelpers": "",\n' +
        '                "schema:workHours": "",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "1893",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1678",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7543",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1978",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1588",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "1892",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "6782",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7839",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "9717",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "7189",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8192",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8929",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "8977",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "9202",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sanitätshelfer"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "10196",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  }\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "67419",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "67419",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')}

function loadRZUb(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "234967",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "5631560",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "234967",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "234967",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Zell",\n' +
        '                      "schema:addressRegion": "Trier",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                      "schema:addressLocality": "Zell",\n' +
        '                      "schema:addressRegion": "Trier",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "234967",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": "00:00:12:00"\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "234967",\n' +
        '                "pairs:TotalNumberOfHelpers": "9",\n' +
        '                "schema:workHours": "81",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "3652",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3791",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3667",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3942",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3988",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3956",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3544",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "3462",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2784",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  }\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "234967",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "234967",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')}

function loadRCUb(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "87629",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "5631560",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "87629",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "87629",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Cochem",\n' +
        '                      "schema:addressRegion": "Trier",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                    "schema:addressLocality": "Cochem",\n' +
        '                    "schema:addressRegion": "Trier",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "87629",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": "00:09:40:00"\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "87629",\n' +
        '                "pairs:TotalNumberOfHelpers": "4",\n' +
        '                "schema:workHours": "93",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "16543",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16783",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16890",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Kraftfahrwesen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16542",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16578",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16589",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16890",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "16432",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  }\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "87629",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "87629",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')}

function loadRBernUb(){
    return JSON.parse('{\n' +
        '        "@context": [\n' +
        '            {\n' +
        '                "schema": "http://schema.org",\n' +
        '                "dct": "http://purl.org/dc/terms/",\n' +
        '                "dcat": "http://www.w3.org/ns/dcat#",\n' +
        '                "pairs": "https://www.pairs-projekt.de/",\n' +
        '                "foaf": "http://xmlns.com/foaf/0.1/",\n' +
        '                "lode": "https://linkedevents.org/ontology/",\n' +
        '                "empathi": "https://w3id.org/empathi/1.0"\n' +
        '            }\n' +
        '        ],\n' +
        '        "scenarioPattern":[\n' +
        '          {\n' +
        '              "@id": "78942",\n' +
        '              "schema:identifier": {\n' +
        '                "@id": "5631560",\n' +
        '                  "schema:startDate": "14/11/2023",\n' +
        '                  "schema:endDate": "15/11/2023"\n' +
        '              },\n' +
        '              "pairs:Context": {\n' +
        '                  "@id": "78942",\n' +
        '                  "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Naturereignissen und anthropogenen Umwelteinflüssen",\n' +
        '                  "Lode:Event": "Starkregen, Hagel, Eisregen, Blitzeis",\n' +
        '                  "pairs:Subevent": "Starkregen"\n' +
        '              },\n' +
        '              "dct:Provenance":{\n' +
        '                  "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
        '                  },\n' +
        '              "schema:location": {\n' +
        '                "@id": "78942",\n' +
        '                  "pairs:ReportLocation": {\n' +
        '                      "schema:addressLocality": "Bernkastel-Kues",\n' +
        '                      "schema:addressRegion": "Wittlich",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  },\n' +
        '                  "pairs:OperationLocation": {\n' +
        '                    "schema:addressLocality": "Bernkastel-Kues",\n' +
        '                    "schema:addressRegion": "Wittlich",\n' +
        '                      "schema:State": "Rheinland-Pfalz",\n' +
        '                      "schema:addressCountry": "Germany"\n' +
        '                  }\n' +
        '              },\n' +
        '              "pairs:Reason": {\n' +
        '                  "pairs:Precondition": "Starkregen"\n' +
        '              },\n' +
        '              "pairs:Impact": {\n' +
        '                  "@id": "78942",\n' +
        '                  "pairs:Postcondition": "",\n' +
        '                  "schema:Duration": "00:18:00:00"\n' +
        '              },\n' +
        '              "foaf:Agent": {\n' +
        '                "@id": "78942",\n' +
        '                "pairs:TotalNumberOfHelpers": "10",\n' +
        '                "schema:workHours": "142",\n' +
        '                "beAware:Responder":[{\n' +
        '                  "pairs:UnitName": "Fachgruppe Wasserschaden/Pumpen B",\n' +
        '                  "pairs:UnitDescription": " Die Fachgruppe Wasserschaden/Pumpen (B) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. In der Sollaufstellung nach Rahmenkonzept soll die Fachgruppe Wasserschaden/Pumpen in der 2,5- fachen Anzahl der Regionalbereiche eines Landesverbandes disloziert werden. Dies entspricht derzeit einer Gesamtzahl von 165 Fachgruppen Wasserschaden/Pumpen.",\n' +
        '                  "pairs:UnitStrength": "-/3/9/12 (+12)",\n' +
        '                  "pairs:Role": [{\n' +
        '                    "schema:name":"Gruppenführer/in",\n' +
        '                    "pairs:NumberOfActors": "1",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Truppführer/in",\n' +
        '                    "pairs:NumberOfActors": "2",\n' +
        '                    "pairs:ActorFunction": "Sprechfunker/in"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "schema:name":"Fachhelfer/in",\n' +
        '                    "pairs:NumberOfActors": "4",\n' +
        '                    "pairs:ActorFunction": "Atemschutzgeräteträger/in, CBRN-Helfer/in, Maschinist/in Pumpen, Kraftfahrer/in CE, Sprechfunker/in, Sanitätshelfer/in"\n' +
        '                  }],\n' +
        '                  "schema:Person": [\n' +
        '                  {\n' +
        '                    "@id": "2763",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2799",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2578",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2542",\n' +
        '                    "schema:gender": "Weiblich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2679",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Sprechfunker"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2655",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2654",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Fachausbildung Wasserschaden / Pumpen"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2998",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Bereichsausbildung Atemschutz"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2699",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  },\n' +
        '                  {\n' +
        '                    "@id": "2678",\n' +
        '                    "schema:gender": "Männlich",\n' +
        '                    "pairs:Qualification": "Grundausbildung"\n' +
        '                  }\n' +
        '                  ]\n' +
        '                }]\n' +
        '              },\n' +
        '              "beAware:Mission": {\n' +
        '                "@id": "78942",\n' +
        '                  "pairs:ActionType": "Bekämpfung von Überschwemmungen/Überflutungen",\n' +
        '                  "schema:Action": ["Netz- und Leitungsbau (Abwasser, groß),Pumparbeiten (klein),Pumparbeiten (groß),Pumparbeiten mit Großpumpe (mittel)"]\n' +
        '              },\n' +
        '              "pairs:Resource": {\n' +
        '                "@id": "78942",\n' +
        '                  "beAware:Vehicle": ["Lastkraftwagen Plane/Spriegel mit Ladebordwand (7 t Nutzlast),Mannschaftslastwagen IV Plane/Spriegel mit Ladebordwand,Anhänger mit Schmutzwasser-Kreiselpumpe (15.000 l/min),Anhänger Plane/Spriegel mit Aufnahmen für Container (7 t Zuladung)"],\n' +
        '                "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
        '              }\n' +
        '          }\n' +
        '        ]\n' +
        '      }\n')}


        function loadFMO(){
          var x = JSON.parse('{\n' +
                '  "@context": [\n' +
                '    {\n' +
                '      "schema": "http://schema.org",\n' +
                '      "dct": "http://purl.org/dc/terms/",\n' +
                '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
                '      "pairs": "https://www.pairs-projekt.de/",\n' +
                '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
                '      "lode": "https://linkedevents.org/ontology/",\n' +
                '      "empathi": "https://w3id.org/empathi/1.0"\n' +
                '    }\n' +
                '  ],\n' +
                '  "scenarioPattern": [\n' +
                '    {\n' +
                '      "schema:identifier": {\n' +
                '        "@id": "917643",\n' +
                '        "schema:startDate": "14/11/2023",\n' +
                '        "schema:endDate": "15/11/2023"\n' +
                '      },\n' +
                '      "pairs:Context": {\n' +
                '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
                '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
                '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
                '        "schema:description": ""\n' +
                '      },\n' +
                '      "dct:Provenance": {\n' +
                '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
                '      },\n' +
                '      "schema:location": {\n' +
                '        "pairs:ReportLocation": {\n' +
                '          "schema:addressLocality": "Mülheim",\n' +
                '          "schema:addressRegion": "Mülheim",\n' +
                '          "schema:State": "Rheinland-Pfalz",\n' +
                '          "schema:addressCountry": "Germany"\n' +
                '        },\n' +
                '        "pairs:OperationLocation": {\n' +
                '          "schema:addressLocality": "Mülheim",\n' +
                '          "schema:addressRegion": "Mülheim",\n' +
                '          "schema:State": "Rheinland-Pfalz",\n' +
                '          "schema:addressCountry": "Germany"\n' +
                '        }\n' +
                '      },\n' +
                '      "pairs:Reason": {\n' +
                '        "pairs:Precondition": "Starkregen"\n' +
                '      },\n' +
                '      "pairs:Impact": {\n' +
                '        "pairs:Postcondition": "",\n' +
                '        "schema:Duration": ""\n' +
                '      },\n' +
                '      "foaf:Agent": {\n' +
                '        "pairs:TotalNumberOfHelpers": "",\n' +
                '        "pairs:DutyHours": "",\n' +
                '        "beAware:Responder": [\n' +
                '          {\n' +
                '            "pairs:UnitName": "Ortungstrupp Typ A",\n' +
                '            "pairs:UnitDescription": "Die Fachgruppe Ortung (A) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. Die Fachgruppe Ortung (A) kann überall dort disloziert werden, wo biologische und technische Or- tung innerhalb einer Teileinheit durchgeführt werden soll. Grundsätzlich sollten diese Aufgaben in den spezialisierten Fachgruppen wahrgenommen werden.",\n' +
                '            "pairs:UnitStrength": "-/2/7/9 (+9)",\n' +
                '            "pairs:Role": [\n' +
                '              {\n' +
                '                "schema:name": "Gruppenführer/in",\n' +
                '                "pairs:NumberOfActors": "1",\n' +
                '                "pairs:ActorFunction": "Technische/r Berater/in Ortung"\n' +
                '              },\n' +
                '              {\n' +
                '                "schema:name": "Truppführer/in",\n' +
                '                "pairs:NumberOfActors": "1",\n' +
                '                "pairs:ActorFunction": "Sprechfunker/in"\n' +
                '              },\n' +
                '              {\n' +
                '                "schema:name": "Fachhelfer/in",\n' +
                '                "pairs:NumberOfActors": "7",\n' +
                '                "pairs:ActorFunction": "Bediener/in technisches Ortungs- gerät, Kraftfahrer/in BE, Rettungshundeführer/in, Sanitätshelfer/in,Sprechfunker/in"\n' +
                '              }\n' +
                '            ],\n' +
                '            "schema:Person": [\n' +
                '              {\n' +
                '                "@id": "15333",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Fachausbildung Ortung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15245",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Ausbilder Kraftfahrer"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15246",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15367",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15369",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15666",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Bereichsausbildung Sprechfunk-Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15646",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15632",\n' +
                '                "schema:gender": "Weiblich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15698",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Bereichsausbildung Sprechfunker - Analog"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15829",\n' +
                '                "schema:gender": "Weiblich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15816",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              },\n' +
                '              {\n' +
                '                "@id": "15943",\n' +
                '                "schema:gender": "Männlich",\n' +
                '                "pairs:Qualification": "Grundausbildung"\n' +
                '              }\n' +
                '            ]\n' +
                '          }\n' +
                '        ]\n' +
                '      },\n' +
                '      "beAware:Mission": {\n' +
                '        "@id": "917643",\n' +
                '        "pairs:ActionType": "Ortungs-, Rettungs-, Bergungsmaßnahmen",\n' +
                '        "schema:Action": [\n' +
                '          "Orten (biologisch),Orten (technisch, Boden),Bergen/Retten von Personen (leicht),Absperren/Absichern,Erkunden (Boden),Ersthelfen,Führen,Eigenschutz,Transportfähigkeit sicherstellen"\n' +
                '        ]\n' +
                '      },\n' +
                '      "pairs:Resource": {\n' +
                '        "@id": "917643",\n' +
                '        "beAware:Vehicle": [\n' +
                '          "Mannschaftstransportwagen TZ,Anhänger mit Spezialaufbau FGr O (2 t Zuladung)"\n' +
                '        ],\n' +
                '      "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
                '      }\n' +
                '    }\n' +
                '  ]\n' +
                '}\n')

              return x;}


              function loadRBernFue(){
                  var x = JSON.parse('{\n' +
                      '  "@context": [\n' +
                      '    {\n' +
                      '      "schema": "http://schema.org",\n' +
                      '      "dct": "http://purl.org/dc/terms/",\n' +
                      '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
                      '      "pairs": "https://www.pairs-projekt.de/",\n' +
                      '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
                      '      "lode": "https://linkedevents.org/ontology/",\n' +
                      '      "empathi": "https://w3id.org/empathi/1.0"\n' +
                      '    }\n' +
                      '  ],\n' +
                      '  "scenarioPattern": [\n' +
                      '    {\n' +
                      '      "schema:identifier": {\n' +
                      '        "@id": "789453",\n' +
                      '        "schema:startDate": "14/11/2023",\n' +
                      '        "schema:endDate": "15/11/2023"\n' +
                      '      },\n' +
                      '      "pairs:Context": {\n' +
                      '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
                      '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
                      '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
                      '        "schema:description": ""\n' +
                      '      },\n' +
                      '      "dct:Provenance": {\n' +
                      '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
                      '      },\n' +
                      '      "schema:location": {\n' +
                      '        "pairs:ReportLocation": {\n' +
                      '          "schema:addressLocality": "Bernkastel-Kues",\n' +
                      '          "schema:addressRegion": "Wittlich",\n' +
                      '          "schema:State": "Rheinland-Pfalz",\n' +
                      '          "schema:addressCountry": "Germany"\n' +
                      '        },\n' +
                      '        "pairs:OperationLocation": {\n' +
                      '          "schema:addressLocality": "Bernkastel-Kues",\n' +
                      '          "schema:addressRegion": "Wittlich",\n' +
                      '          "schema:State": "Rheinland-Pfalz",\n' +
                      '          "schema:addressCountry": "Germany"\n' +
                      '        }\n' +
                      '      },\n' +
                      '      "pairs:Reason": {\n' +
                      '        "pairs:Precondition": "Starkregen"\n' +
                      '      },\n' +
                      '      "pairs:Impact": {\n' +
                      '        "pairs:Postcondition": "",\n' +
                      '        "schema:Duration": "00:17:00:00"\n' +
                      '      },\n' +
                      '      "foaf:Agent": {\n' +
                      '        "pairs:TotalNumberOfHelpers": "13",\n' +
                      '        "pairs:DutyHours": "236",\n' +
                      '        "beAware:Responder": [\n' +
                      '          {\n' +
                      '            "pairs:UnitName": "Ortungstrupp Typ A",\n' +
                      '            "pairs:UnitDescription": "Die Fachgruppe Ortung (A) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. Die Fachgruppe Ortung (A) kann überall dort disloziert werden, wo biologische und technische Or- tung innerhalb einer Teileinheit durchgeführt werden soll. Grundsätzlich sollten diese Aufgaben in den spezialisierten Fachgruppen wahrgenommen werden.",\n' +
                      '            "pairs:UnitStrength": "-/2/7/9 (+9)",\n' +
                      '            "pairs:Role": [\n' +
                      '              {\n' +
                      '                "schema:name": "Gruppenführer/in",\n' +
                      '                "pairs:NumberOfActors": "1",\n' +
                      '                "pairs:ActorFunction": "Technische/r Berater/in Ortung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "schema:name": "Truppführer/in",\n' +
                      '                "pairs:NumberOfActors": "1",\n' +
                      '                "pairs:ActorFunction": "Sprechfunker/in"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "schema:name": "Fachhelfer/in",\n' +
                      '                "pairs:NumberOfActors": "7",\n' +
                      '                "pairs:ActorFunction": "Bediener/in technisches Ortungs- gerät, Kraftfahrer/in BE, Rettungshundeführer/in, Sanitätshelfer/in,Sprechfunker/in"\n' +
                      '              }\n' +
                      '            ],\n' +
                      '            "schema:Person": [\n' +
                      '              {\n' +
                      '                "@id": "1854",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Fachausbildung Ortung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1892",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1743",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1811",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1488",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1489",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Ausbilder Kraftfahrer"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1467",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1890",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1864",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1489",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Bereichsausbildung Sprechfunk-Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1876",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1456",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1444",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              }\n' +
                      '            ]\n' +
                      '          }\n' +
                      '        ]\n' +
                      '      },\n' +
                      '      "beAware:Mission": {\n' +
                      '        "@id": "7943",\n' +
                      '        "pairs:ActionType": "Ortungs-, Rettungs-, Bergungsmaßnahmen",\n' +
                      '        "schema:Action": [\n' +
                      '          "Orten (biologisch),Orten (technisch, Boden),Bergen/Retten von Personen (leicht),Absperren/Absichern,Erkunden (Boden),Ersthelfen,Führen,Eigenschutz,Transportfähigkeit sicherstellen"\n' +
                      '        ]\n' +
                      '      },\n' +
                      '      "pairs:Resource": {\n' +
                      '        "@id": "7943",\n' +
                      '        "beAware:Vehicle": [\n' +
                      '          "Mannschaftstransportwagen TZ,Anhänger mit Spezialaufbau FGr O (2 t Zuladung)"\n' +
                      '        ],\n' +
                      '      "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
                      '      }\n' +
                      '    }\n' +
                      '  ]\n' +
                      '}\n')
                    return x}

              function loadFBernO(){
                  var x = JSON.parse('{\n' +
                      '  "@context": [\n' +
                      '    {\n' +
                      '      "schema": "http://schema.org",\n' +
                      '      "dct": "http://purl.org/dc/terms/",\n' +
                      '      "dcat": "http://www.w3.org/ns/dcat#",\n' +
                      '      "pairs": "https://www.pairs-projekt.de/",\n' +
                      '      "foaf": "http://xmlns.com/foaf/0.1/",\n' +
                      '      "lode": "https://linkedevents.org/ontology/",\n' +
                      '      "empathi": "https://w3id.org/empathi/1.0"\n' +
                      '    }\n' +
                      '  ],\n' +
                      '  "scenarioPattern": [\n' +
                      '    {\n' +
                      '      "schema:identifier": {\n' +
                      '        "@id": "789453",\n' +
                      '        "schema:startDate": "14/11/2023",\n' +
                      '        "schema:endDate": "15/11/2023"\n' +
                      '      },\n' +
                      '      "pairs:Context": {\n' +
                      '        "empathi:HazardType": "Gefahren und Anforderungen aufgrund von Natur- ereignissen und anthropogenen Umwelteinflüssen",\n' +
                      '        "Lode:Event": "Hochwasser/Sturmfluten",\n' +
                      '        "pairs:Subevent": "Hochwasser in Bächen, Flüssen und Stromtälern",\n' +
                      '        "schema:description": ""\n' +
                      '      },\n' +
                      '      "dct:Provenance": {\n' +
                      '        "schema:Organization": "Technisches Hilfswerk (THW)"\n' +
                      '      },\n' +
                      '      "schema:location": {\n' +
                      '        "pairs:ReportLocation": {\n' +
                      '          "schema:addressLocality": "Bernkastel-Kues",\n' +
                      '          "schema:addressRegion": "Wittlich",\n' +
                      '          "schema:State": "Rheinland-Pfalz",\n' +
                      '          "schema:addressCountry": "Germany"\n' +
                      '        },\n' +
                      '        "pairs:OperationLocation": {\n' +
                      '          "schema:addressLocality": "Bernkastel-Kues",\n' +
                      '          "schema:addressRegion": "Wittlich",\n' +
                      '          "schema:State": "Rheinland-Pfalz",\n' +
                      '          "schema:addressCountry": "Germany"\n' +
                      '        }\n' +
                      '      },\n' +
                      '      "pairs:Reason": {\n' +
                      '        "pairs:Precondition": "Starkregen"\n' +
                      '      },\n' +
                      '      "pairs:Impact": {\n' +
                      '        "pairs:Postcondition": "",\n' +
                      '        "schema:Duration": "00:17:00:00"\n' +
                      '      },\n' +
                      '      "foaf:Agent": {\n' +
                      '        "pairs:TotalNumberOfHelpers": "13",\n' +
                      '        "pairs:DutyHours": "236",\n' +
                      '        "beAware:Responder": [\n' +
                      '          {\n' +
                      '            "pairs:UnitName": "Ortungstrupp Typ A",\n' +
                      '            "pairs:UnitDescription": "Die Fachgruppe Ortung (A) ist als Fachgruppe im Technischen Zug eine Teileinheit im THW. Die Fachgruppe Ortung (A) kann überall dort disloziert werden, wo biologische und technische Or- tung innerhalb einer Teileinheit durchgeführt werden soll. Grundsätzlich sollten diese Aufgaben in den spezialisierten Fachgruppen wahrgenommen werden.",\n' +
                      '            "pairs:UnitStrength": "-/2/7/9 (+9)",\n' +
                      '            "pairs:Role": [\n' +
                      '              {\n' +
                      '                "schema:name": "Gruppenführer/in",\n' +
                      '                "pairs:NumberOfActors": "1",\n' +
                      '                "pairs:ActorFunction": "Technische/r Berater/in Ortung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "schema:name": "Truppführer/in",\n' +
                      '                "pairs:NumberOfActors": "1",\n' +
                      '                "pairs:ActorFunction": "Sprechfunker/in"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "schema:name": "Fachhelfer/in",\n' +
                      '                "pairs:NumberOfActors": "7",\n' +
                      '                "pairs:ActorFunction": "Bediener/in technisches Ortungs- gerät, Kraftfahrer/in BE, Rettungshundeführer/in, Sanitätshelfer/in,Sprechfunker/in"\n' +
                      '              }\n' +
                      '            ],\n' +
                      '            "schema:Person": [\n' +
                      '              {\n' +
                      '                "@id": "1854",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Fachausbildung Ortung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1892",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1743",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1811",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1488",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1489",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Ausbilder Kraftfahrer"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1467",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1890",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1864",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1489",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Bereichsausbildung Sprechfunk-Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1876",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1456",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              },\n' +
                      '              {\n' +
                      '                "@id": "1444",\n' +
                      '                "schema:gender": "Männlich",\n' +
                      '                "pairs:Qualification": "Grundausbildung"\n' +
                      '              }\n' +
                      '            ]\n' +
                      '          }\n' +
                      '        ]\n' +
                      '      },\n' +
                      '      "beAware:Mission": {\n' +
                      '        "@id": "7943",\n' +
                      '        "pairs:ActionType": "Ortungs-, Rettungs-, Bergungsmaßnahmen",\n' +
                      '        "schema:Action": [\n' +
                      '          "Orten (biologisch),Orten (technisch, Boden),Bergen/Retten von Personen (leicht),Absperren/Absichern,Erkunden (Boden),Ersthelfen,Führen,Eigenschutz,Transportfähigkeit sicherstellen"\n' +
                      '        ]\n' +
                      '      },\n' +
                      '      "pairs:Resource": {\n' +
                      '        "@id": "7943",\n' +
                      '        "beAware:Vehicle": [\n' +
                      '          "Mannschaftstransportwagen TZ,Anhänger mit Spezialaufbau FGr O (2 t Zuladung)"\n' +
                      '        ],\n' +
                      '      "schema:instrument": ["Schmutzwasser-Kreiselpumpe mit einer Leistung von 5.000, 15.000 oder 25.000 Litern pro Minute, Pumpensatz (8 Tauchpumpen mit 1.000 bis 3.000 Litern pro Minute), Werkstattausstattung Abwasserschäden,Pumpenzubehör, Energieverteilersatz 32/16 A, Brenner-Ausstattung Propangas, Vermessungsausstattung, Flutlichtleuchtensatz 1 kW, Schlauchpflegegerät groß, Trennschleifgerät elektrisch 230 V, Stromerzeuger 8 kVA 230/400 V 50/60Hz,Schläuche"]\n' +
                      '      }\n' +
                      '    }\n' +
                      '  ]\n' +
                      '}\n')
                    return x}
