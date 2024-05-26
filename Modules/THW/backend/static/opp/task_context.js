function createActionItem(action, i) {

    // item with header
    var accordionItem = $(`
        <div class="accordion-item">
        </div>
    `);

    var itemHeader = $(`
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#actionCollapse${i}">
                ${action.name}
            </button>
        </h2>
    `);
    accordionItem.append(itemHeader);

    var itemCollapse = $(`
        <div id="actionCollapse${i}" class="accordion-collapse collapse" data-bs-parent="#actionAccordion">
        </div>
    `);
    accordionItem.append(itemCollapse)

    var collapseBody = $(`
        <div class="accordion-body">
           <table class="table table-bordered">
              <tbody>
                <tr>
                  <th scope="row">Description</th>
                  <td>${action.description}</td>
                </tr>
                <tr>
                  <th scope="row">Category</th>
                  <td>${action.category}</td>
                </tr>
              </tbody>
            </table>
        </div>
    `);
    itemCollapse.append(collapseBody);

    var detailsAccordion = $(`
        <div class="accordion" id="actionDetailsAccordion${i}">
        </div>
    `);
    collapseBody.append(detailsAccordion);

    return accordionItem;
}


function updateActions(actions) {

    var subevent_name = getSelectedSubevent();
    var location_city = getSelectedCity();
    var actionType_name = getSelectedActionType();
    var data = queryLocationSubeventActiontypeAction(location_city, subevent_name, actionType_name);

    var accordion = $("#actionAccordion");
    accordion.empty();
    accordion.append(loading());

    data.then(function (data) {

        accordion.empty();
        if (!("data" in data) || !(data["data"])) {
            accordion.append($("<strong>No actions found.</strong>"));
            return;
        }
        actions = data["data"]

        var elements = $();
        actions.forEach(function (action, i) {
            elements = elements.add(createActionItem(action, i));
        });
        accordion.append(elements);
    })

}


$(function () {
})
