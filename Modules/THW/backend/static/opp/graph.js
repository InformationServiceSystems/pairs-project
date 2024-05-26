function renderGraph(location_city, subevent_name) {
    var subevent_name = getSelectedSubevent();
    var location_city = getSelectedCity();
    var query = `
    MATCH
    (location:Location WHERE location.city =~ "(?i).*${location_city}.*")
        - [r1:t_happens_at] -
        (sp:ScenarioPattern)
        - [r2:t_identified_by] -
        (subevent:Subevent WHERE subevent.name =~ "(?i).*${subevent_name}.*")
    MATCH (sp) - [r3:t_involves] - (actor:Actors)
    MATCH (sp) - [r4:t_creates] - (impact:Impact)
    MATCH (sp) - [r5:t_caused_by] - (reason:Reason)
    MATCH (sp) - [r6:t_described_by] - (provenance:Provenance)
    MATCH (sp) - [r7:t_bounded_by] - (context:Context)
    RETURN * limit 100
    `;

    const config = {
        containerId: "graph",
        neo4j: {
            serverUrl: "bolt://localhost:7687",
            serverUser: "neo4j",
            serverPassword: "OperationsPlanning",
        },
        //visConfig: {
            //physics: {
                //enabled: false
                //}
            //},
        labels: {
            Location: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "LightSeaGreen"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Subevent: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "Khaki"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Actor: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "Lavender"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Impact: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "DarkSalmon"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Reason: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "LawnGreen"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Provenance: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "SaddleBrown"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            Context: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "LightBlue"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },
            ScenarioPattern: {
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        color: "LightCoral"
                    },
                    function: {
                        title: NeoVis.objectToTitleHtml
                    }
                }
            },

        },
        //relationships: {
            //INTERACTS: {
                //value: "weight"
                //}
            //},
        initialCypher: query
    };

    var neoVis = new NeoVis.default(config);
    neoVis.render();

}

$(function () {
});
