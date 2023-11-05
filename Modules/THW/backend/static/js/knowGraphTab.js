var data = graphData.graph_data
var links = []
var nodes = []
console.log(data)

//LINKS
for (var i = 0; i < data.length; i++){
   // console.log(data[i])
    links[i] = {"source": data[i].a.id, "target": data[i].b.id, "name":  data[i].r[1]}  
}
//33333333333
for (var i = 0; i < data.length; i++){
    // var obj1 = { "id": data[i].a.id };
    // var obj2 = { "id": data[i].b.id };
    
    nodes.push(data[i].a);
    nodes.push(data[i].b);
}

var uniqueIds = [];
var filteredNodes = [];

for (var i = 0; i < nodes.length; i++) {
    var id = nodes[i].id;
    if (!uniqueIds.includes(id)) {
        uniqueIds.push(id);
        filteredNodes.push(nodes[i]);
    }
}

console.log(filteredNodes)
console.log(links)

// Apply label truncation to the data nodes

var container_kg = document.getElementById('graph-container');
var data_kg = {

    nodes: new vis.DataSet(filteredNodes.map(function(node) {
        if (node.id.length > 6) {
            node.label = node.id.substring(0, 6) + '...';
        }else{
            node.label = node.id;
        }
        return {
            id: node.id,
            label: node.label,
            color: '#d6d2fa'
        };
    })),

    edges: new vis.DataSet(links.map(function(links) {
        return {
            from: links.source,
            to: links.target,
            label: links.name
        };
    }))
};

var options_kg = {};

var network_kg = new vis.Network(container_kg, data_kg, options_kg);

network_kg.moveTo({
    position: {x:900000.0,y:90000.0},
    scale: 0.5 ,
    offset:{x: 0,y:0},
    animation: true
});

function createPopupContent(nodeId) {
    var popupContent = '';

    for (let index = 0; index < filteredNodes.length; index++) {

        if( filteredNodes[index].id == nodeId ) {

            for (var key in filteredNodes[index]) {
                if (filteredNodes[index].hasOwnProperty(key)) {
                    popupContent += key + ': ' + filteredNodes[index][key] + '<br>';
                }
            }
        }
        
    }

   
    return popupContent;
}

// Attach a click event listener to the graph
network_kg.on('click', function(event) {
    console.log(event)
    var nodeId = event.nodes[0]; // Get the clicked node's ID  
    if (nodeId) {
        var popupContainer = document.getElementById('graph-container-popup');
        var existingPopup = popupContainer.querySelector('.popup_graph_kg');
        // Check if there is an existing popup
        if (existingPopup) {
            popupContainer.removeChild(existingPopup);
        }
        var popup = document.createElement('div');
        popup.className = 'popup_graph_kg';
        popup.innerHTML  = createPopupContent(nodeId);
        popupContainer.appendChild(popup);

        setTimeout(function() {
            if (existingPopup) {
                document.getElementById('graph-container-popup').removeChild(popup);
            }
        }, 5000);

    }
});