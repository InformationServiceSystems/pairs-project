const selectEvent = document.getElementById('events-dropdown');
const selectAction = document.getElementById('actions-dropdown');
const selectCity = document.getElementById('city-dropdown-r');

var selectedEvent = '';
var selectedCity = '';
var selectedAction = '';

function updateUI(){
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
    if (selectedText_event === 'Hochwasser' && selectedText_action === 'Ortungs-, Rettungs-, Bergungsmaßnahmen') {
        jsonData = JSON.parse(jsonFloodOrd.innerHTML);
    } else if (selectedText_event === 'Starkregen' && selectedText_action === 'Führung, Führungsunterstützung und Verbindung') {
        jsonData = JSON.parse(jsonStarkregenF.innerHTML);
    }else if (selectedText_event === 'Hochwasser' && selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen') {
        jsonData = JSON.parse(jsonFloodBek.innerHTML);
    }else if (selectedText_event === 'Starkregen' && selectedText_action === 'Bekämpfung von Überschwemmungen/Überflutungen') {
        jsonData = JSON.parse(jsonStarkregenBek.innerHTML);
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
    }
}
