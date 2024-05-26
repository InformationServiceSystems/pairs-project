function createUnitItem(unit, i) {

    // item with header
    var accordionItem = $(`
        <div class="accordion-item">
        </div>
    `);

    var itemHeader = $(`
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#unitCollapse${i}">
                ${unit.name}
            </button>
        </h2>
    `);
    accordionItem.append(itemHeader);

    var itemCollapse = $(`
        <div id="unitCollapse${i}" class="accordion-collapse collapse" data-bs-parent="#unitAccordion">
        </div>
    `);
    accordionItem.append(itemCollapse)

    var collapseBody = $(`
        <div class="accordion-body">
           <table class="table table-bordered">
              <tbody>
                <tr>
                  <th scope="row">Abbreviation</th>
                  <td>${unit.abbreviation}</td>
                </tr>
                <tr>
                  <th scope="row">Strength</th>
                  <td>${unit.strength}</td>
                </tr>
                <tr>
                  <th scope="row">Description</th>
                  <td colspan="2">${unit.description}</td>
                </tr>
              </tbody>
            </table>
        </div>
    `);
    itemCollapse.append(collapseBody);

    var detailsAccordion = $(`
        <div class="accordion" id="unitDetailsAccordion${i}">
        </div>
    `);
    collapseBody.append(detailsAccordion);

    var equipmentAccordionItem = createSubtaskDetailsItem(unit, i);
    detailsAccordion.append(equipmentAccordionItem);

    var vehicleAccordionItem = createVehicleDetailsItem(unit, i);
    detailsAccordion.append(vehicleAccordionItem);

    var functionAccordionItem = createFunctionDetailsItem(unit, i);
    detailsAccordion.append(functionAccordionItem);
    return accordionItem;
}


function createSubtaskDetailsItem(unit, i) {

    var accordionItem = $(`
        <div class="accordion-item">
        </div>
    `);

    var accordionHeader = $(`
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#unitEquipmentDetailsCollapse${i}">
                Equipment
            </button>
        </h2>
    `);
    accordionItem.append(accordionHeader);

    var accordionCollapse = $(`
        <div id="unitEquipmentDetailsCollapse${i}" class="accordion-collapse collapse" data-bs-parent="#unitDetailsAccordion${i}">
        </div>
    `);
    accordionItem.append(accordionCollapse);

    var collapseBody = $(`
        <div class="accordion-body">
        </div>
    `);
    accordionCollapse.append(collapseBody);

    var table = $(`
       <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">Number</th>
              <th scope="col">Name</th>
            </tr>
          </thead>
        </table>
    `);
    collapseBody.append(table);

    var body = $(`
      <tbody>
      </tbody>
    `);

    table.append(body);

    var data = queryUnitEquipment(unit.name);
    data.then(function (data) {

        if (!("data" in data) || !(data["data"])) {
            return;
        }
        equipments = data["data"];
        equipments.forEach(function (equipment, i) {
            body.append($(`
                    <tr>
                      <th scope="row">${equipment.number}</td>
                      <td>${equipment.name}</td>
                    </tr>
                `));
        });
    });

    return accordionItem;
}


function createVehicleDetailsItem(unit, i) {

    var accordionItem = $(`
        <div class="accordion-item">
        </div>
    `);

    var accordionHeader = $(`
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#unitVehicleDetailsCollapse${i}">
                Vehicle
            </button>
        </h2>
    `);
    accordionItem.append(accordionHeader);

    var accordionCollapse = $(`
        <div id="unitVehicleDetailsCollapse${i}" class="accordion-collapse collapse" data-bs-parent="#unitDetailsAccordion${i}">
        </div>
    `);
    accordionItem.append(accordionCollapse);

    var collapseBody = $(`
        <div class="accordion-body">
        </div>
    `);
    accordionCollapse.append(collapseBody);

    var table = $(`
       <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">Name</th>
            </tr>
          </thead>
        </table>
    `);
    collapseBody.append(table);

    var body = $(`
      <tbody>
      </tbody>
    `);

    table.append(body);

    var data = queryUnitVehicle(unit.name);
    data.then(function (data) {

        if (!("data" in data) || !(data["data"])) {
            return;
        }
        vehicles = data["data"];
        vehicles.forEach(function (vehicle, i) {
            body.append($(`
                    <tr>
                      <td>${vehicle.name}</td>
                    </tr>
                `));
        });
    });

    return accordionItem;
}

function createFunctionDetailsItem(unit, i) {

    var accordionItem = $(`
        <div class="accordion-item">
        </div>
    `);

    var accordionHeader = $(`
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#unitFunctionDetailsCollapse${i}">
                Function
            </button>
        </h2>
    `);
    accordionItem.append(accordionHeader);

    var accordionCollapse = $(`
        <div id="unitFunctionDetailsCollapse${i}" class="accordion-collapse collapse" data-bs-parent="#unitDetailsAccordion${i}">
        </div>
    `);
    accordionItem.append(accordionCollapse);

    var collapseBody = $(`
        <div class="accordion-body">
        Select a row to get more details about the selected function.
        <br>
        </div>
    `);
    accordionCollapse.append(collapseBody);

    var table = $(`
       <table class="table table-bordered table-hover">
          <thead>
            <tr>
              <th scope="col">Number</th>
              <th scope="col">Name</th>
            </tr>
          </thead>
        </table>
    `);
    collapseBody.append(table);

    var body = $(`
      <tbody>
      </tbody>
    `);

    table.append(body);

    var data = queryUnitFunction(unit.name);
    data.then(function (data) {

        if (!("data" in data) || !(data["data"])) {
            return;
        }
        functions = data["data"];
        functions.forEach(function (fun, j) {
            var row = $(`
                <tr class="clickable-row">
                  <th scope="row" class="number">${fun.number}</td>
                  <td class="name">${fun.name}</td>
                </tr>
            `);
            row.click(function() {
                $(`#qualificationDetails${i}`).remove()
                var qualificationDetails = createQualificationDetails(fun.name, i);
                collapseBody.append(qualificationDetails);
            });
            body.append(row);
        });
    });

    return accordionItem;
}

function createQualificationDetails(function_name, i) {

    var qualificationDetails = $(`<div id="qualificationDetails${i}"></div>`);
    var a = $(`
      <a href="#" class="d-inline-block me-2" data-bs-toggle="tooltip" data-bs-title="Default tooltip">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"></path>
          <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0"></path>
        </svg>
      </a>
    `);
    qualificationDetails.append(a);
    new bootstrap.Tooltip(a);
    qualificationDetails.append(`Displaying details for <strong>${function_name}</strong>.<br>`);
    qualificationDetails.append("Select a row to get more details about the selected qualification.");

    var table = $(`
       <table class="table table-bordered table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
            </tr>
          </thead>
        </table>
    `);
    qualificationDetails.append(table);

    var body = $(`
      <tbody>
      </tbody>
    `);
    table.append(body);
    var data = queryFunctionQualification(function_name);
    data.then(function (data) {

        if (!("data" in data) || !(data["data"])) {
            return;
        }
        qualifications = data["data"];
        qualifications.forEach(function (qualification, j) {
            var row = $(`
                <tr>
                  <td>${qualification.name}</td>
                </tr>
            `);
            row.click(function() {
                $(`#personDetails${i}`).remove();
                var personDetails = createPersonDetails(qualification.name, i);
                qualificationDetails.append(personDetails);
            });
            body.append(row);
        });
    });


    return qualificationDetails;
}

function createPersonDetails(function_name, i) {
    var personDetails = $(`<div id="personDetails${i}"></div>`);
    personDetails.append(`Displaying details for <strong>${function_name}</strong>.<br>`);

    var table = $(`
       <table class="table table-bordered">
          <thead>
            <tr>
              <th scope="col">Age</th>
              <th scope="col">Gender</th>
              <th scope="col">Expert</th>
              <th scope="col">Activation Date</th>
            </tr>
          </thead>
        </table>
    `);
    personDetails.append(table);

    var body = $(`
      <tbody>
      </tbody>
    `);
    table.append(body);

    var data = queryQualificationPerson(function_name);
    data.then(function (data) {
        console.log(data)
        if (!("data" in data) || !(data["data"])) {
            return;
        }
        persons = data["data"];
        persons.forEach(function (person, i) {
            var row = $(`
                <tr>
                  <td>${person.age}</td>
                  <td>${person.gender}</td>
                  <td>${person.expert}</td>
                  <td>${person.activation_date}</td>
                </tr>
            `);
            body.append(row);
        });
    });

    return personDetails;
}



function updateUnits(units) {

    var subevent_name = getSelectedSubevent();
    var location_city = getSelectedCity();
    var actionType_name = getSelectedActionType();
    var data = queryLocationSubeventActiontypeUnit(location_city, subevent_name, actionType_name);

    var accordion = $("#unitAccordion");
    accordion.empty();
    accordion.append(loading());

    data.then(function (data) {

        accordion.empty();
        if (!("data" in data) || !(data["data"])) {
            accordion.append($("<strong>No units found.</strong>"));
            return;
        }
        units = data["data"]

        var elements = $();
        units.forEach(function (unit, i) {
            elements = elements.add(createUnitItem(unit, i));
        });
        accordion.append(elements);
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    })

}


$(function () {
})
