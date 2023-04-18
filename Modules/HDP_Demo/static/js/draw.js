let neoViz;

    function draw(container) {


        var initialCypher = "MATCH (n)-[r:produce|is_category|sells|isComponent]->(m) RETURN n,r,m LIMIT 100"

        const config = {
            containerId: container,
            neo4j: {
                serverUrl: "bolt://localhost:7687",
                serverUser: "neo4j",
                serverPassword: "password",
            },
            labels: {
                "component": {
                    label: "ident",
                },
                "category": {
                    label: "name",
                },
                "manufacturer": {
                    label: "name",
                },
                "seller": {
                    label: "name",
                },

                'isComponent':{
                label: "isComponent",
                }
            },
            relationships: {

               "isComponent": {
                    label:'label',

                },
                "is_category": {
                    label: 'label'
                },
                "is_similar": {
                    label: 'label'
                },
                "produce": {
                    label: 'label'
                },
                "sells": {
                    label: 'label'
                }


            },
            initialCypher: initialCypher,


            visConfig: {
				edges: {
					arrows: {
						to: {enabled: true}
					}
				},
			}


        };

        neoViz = new NeoVis.default(config);
        neoViz.render();
    }

    

