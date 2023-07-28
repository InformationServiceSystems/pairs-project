//---------------SET IDs to ALL nodes---------------------
var data = graphData.graph_data
var links = []
var nodes = []

//LINKS
for (var i = 0; i < data.length; i++){
   // console.log(data[i])
    links[i] = {"source": data[i].a.id, "target": data[i].b.id, "name":  data[i].r[1]}  
}
//33333333333
for (var i = 0; i < data.length; i++){
    var obj1 = { "id": data[i].a.id };
    var obj2 = { "id": data[i].b.id };
    
    nodes.push(obj1);
    nodes.push(obj2);
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
//3333333333

const myGraph = ForceGraph3D();

myGraph(document.getElementById('graph-container'))
    .graphData( { nodes: filteredNodes, links:links })
    .height(515)
    .width(1760)
    .nodeLabel('id')
    .backgroundColor('white')
    .linkColor(() => '#999999')
    .nodeRelSize(8)
    .nodeOpacity(1)
    .nodeColor('rgba(0, 136, 204, 0.8)')
    .nodeResolution(32)
    .linkOpacity(0.5)
    .linkCurvature(0.2)
    .linkDirectionalArrowLength(6)
    .linkDirectionalArrowRelPos(1)
    .linkWidth(1)
    //.linkCurvature(0.15)
    .nodeColor('green')
    .d3Force('collide', d3.forceCollide(10)) // Enable collision detection for nodes to prevent overlap
    .d3Force('charge', d3.forceManyBody().strength(-50)) // Adjust the charge force for better node spacing
    .d3Force('link', d3.forceLink().id(d => d.id).distance(50)) // Adjust the link force for better link spacing
    .d3VelocityDecay(0.6); // Adjust the velocity decay for smoother animations

myGraph.nodeThreeObjectExtend(true)
.nodeThreeObject(node => {
    const nodeColor = new THREE.Color('rgba(0, 136, 204, 0.8)');
    const nodeGeometry = new THREE.SphereGeometry(5);
    const nodeMaterial = new THREE.MeshBasicMaterial({ color: nodeColor });
    const nodeMesh = new THREE.Mesh(nodeGeometry, nodeMaterial);

    const group = new THREE.Group();
    group.add(nodeMesh)

    //shorten long node.id
    let labelText = node.id;
    if (node.hasOwnProperty('id')) {
        const nodeName = node.id;
        if (nodeName.length > 20) {
            labelText = nodeName.substring(0, 20) + '...';
        } else {
            labelText = nodeName;
        }
    }else{
        labelText = nodeName;
    }

    const labelSprite = new SpriteText(labelText);
    labelSprite.material.depthWrite = true;
    labelSprite.color = 'black';
    labelSprite.textHeight = 8;
    labelSprite.position.z = 10;

    group.add(labelSprite);
    return group;
})

myGraph
.linkThreeObjectExtend(true)
.linkThreeObject(link => {
    const sprite = new SpriteText(link.name);
    sprite.color = 'black';
    sprite.textHeight = 4.5;
    return sprite;
})
.linkPositionUpdate((sprite, { start, end }) => {
    const middlePos = Object.assign(...['x', 'y', 'z'].map(c => ({
        [c]: start[c] + (end[c] - start[c]) / 2 // calc middle point
    })));
    sprite.position.copy(middlePos);
});

myGraph.nodeColor(node => {
    const coloredNode = nodes.find(n => n.id === node.id);
    if (coloredNode) {
        return coloredNode.color;
    } else {
        return 'rgba(0, 136, 204, 0.8)'; // Default color for other nodes
    }
    });