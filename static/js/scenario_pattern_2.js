const API_URL = 'http://127.0.0.1:8000/OutageForecast';
const CONTAINER_NAME = "scenarioPatternGraph";


/*
    Getting  all data
*/

const pred = [];
const feat = [];
const dat = [];
const conf = [];
const data_filter =[];

function collectData(city){
    const url = 'http://127.0.0.1:8000/OutageForecast/predict/?city='+ city;
    fetch(url).then(response => {
        response.json().then(data=> {
            const predictions = data.Predictions;
            const features = data.Features;
            const data_org = data.Weather;
            const confidence = data.Confidence;
            console.log(features, data_org);
            pred.push(predictions);
            feat.push(features);
            conf.push(confidence);
            dat.push(data_org);

        });
    })
}


/**
 * Returns the timestamp for identifier details
 */
function getTimestamp() {
    // TODO: decide on time format
    return (new Date()).toString();
}

/**
 * Returns the confidenc for a given outage id
 */
 function getConfidence(city , id )     {
    collectData(city);
    console.log("pred, feat,dat, conf ", pred, feat,dat, conf);

    return conf[id];
}

/**
 * Returns the data features for a given city and outage id
 */
function getDataFeatures( city, id ) {
    // TODO: Fetch data from backend when endpoint exists
    collectData(city);
    if (data_filter.length != 0){
        data_filter.splice(0,data_filter.length);
    }
    console.log("id ", id);
    const Features = feat[id];
    const Original = dat[id];
    console.log("Original ", Original);
    console.log("Original[id] ", Original[id]);
    console.log("Features ", Features);

    for (var i = 0; i< 15; i++){
        if(i == 5 || i == 6 || i == 10 || i == 14 ) {
        data_filter.push(Original[id][i]);
        }
    }

    return data_filter;
}

/**
 * Returns all outage ids for a given city up until a given outage id as string
 */
function getOutageIds( city, id ) {
    const ids = [];
    for (let [i, val] of pred.entries()) {
        if (i < id && val == 1) {
            ids.push(i+1);
        }
    }
    if (!ids.length) {
        return "";
    }
    return `outage.${ids.join(', ')}`;
}

function capitalize( str ) {
    return str.charAt(0).toUpperCase() + str.slice(1); 
}

/**
 * Returns the timestamp for identifier details
 */
function dict2Markup( dict ) {
    markup = "";
    for (const [key, value] of Object.entries(dict)) {
        markup += `<b>${capitalize(key)}:</b> ${value}<br>`
    }
    return markup;
}

/**
 * Returns tooltip details for each node as dictionary
 */
async function getNodeInfoDetails( node, city, id) {
    const details = {};
    switch(node) {
        case "Measure":
           details["actionSteps"] = "plan downtime, plan maintenance, controlled shutdown"
           details["category"] = "precautionary";
        break;
        case "Resources":
            details["equipment"] = "none";
        break;
        case "Location":
            details["city"] = city;
            details["region"] = "bavaria";
        break;
        case "ScenarioLocation":
            details["city"] = city;
            details["region"] = "bavaria";
        break;
        case "ImpactLocation":
            details["city"] = city;
            details["region"] = "bavaria";
        break;
        case "Identifier":
            details["id"] = id+1;
            details["title"] = `outage.${id+1}`;
            details["timestamp"] = getTimestamp();
        break;
        case "Context":
            details["scenarioDescription"] = "outage based on shutdown windturbines, power grid fluctuation";
            details["features"] = "Max Wind Speed, Max Wind Gust, Rain Precipitation, Thunder";
            details["data"] = getDataFeatures( city, id );
            details["influentialFactors"] = "season, weather";
        break;
        case "Actors":
            details["actorRole"] = "plant manager";
            details["skillSet"] = "maintainance work, technical expertise";
        break;
        case "History":
            details["identifierIds"] = getOutageIds(city, id);
        break;
        case "Source":
            details["organization"] = "bundesnetzagentur, ncei";
        break;
        case "Reason":
            const confidence = conf[id];
            details["precondition"] = "thunderstorm";
            details["probability"] = confidence || "No outage"
        break;
        case "Effect":
            details["postcondition"] = "machine downtime";
            details["complexity"] = "low"
        break;
        case "Scenario":
        break;
    }
    return details; 
}

/**
 * Charts the scenario graph for the given parameters
 */

function chart( className, city, id ) {
    Highcharts.chart(className, {
        chart: {
            type: 'networkgraph',
            marginTop: 35
        },
        title: {
            text: 'Scenario Pattern'
        },
        tooltip: {
              formatter: async function (tooltip) {
                  const details = await getNodeInfoDetails(this.key, city, id);
                  const info = dict2Markup(details);
                  tooltip.label.attr({
                      text: `<b>${this.key}:</b><br> ${info}`
                  });
                  return "Loading...";
              }
        },
        plotOptions: {
            networkgraph: {
                keys: ['from', 'to'],

              layoutAlgorithm: {
                enableSimulation: true,
                integration: 'verlet',
                linkLength: 70
              }
            }
         },
        series: [{
            marker: {
                radius: 10
            },
        dataLabels: {
            enabled: true,
            linkFormat: '',
            allowOverlap: true
        },
        data: [
                ['Scenario', 'Effect'],
                ['Scenario', 'ScenarioLocation'],
                ['Scenario', 'History'],
                ['Scenario', 'Reason'],
                ['Scenario', 'Source'],
                ['Scenario', 'Context'],
                ['Scenario', 'Actors'],
                ['Scenario', 'Identifier'],
                ['Scenario', 'ImpactLocation'],
                ['ScenarioLocation', 'Location'],
                ['ImpactLocation', 'Location'],
                ['Resources', 'Location'],
                ['Measure', 'Resources'],
                ['Actors', 'Measure']
                ],
            nodes: [{
                  id: 'Scenario'
                }, {
                  id: 'Effect'
                }, {
                  id: 'ScenarioLocation'
                }, {
                  id: 'History'
                }, {
                  id: 'Reason'
                }, {
                  id: 'Source'
                }, {
                  id: 'Context'
                }, {
                  id: 'Actors'
                }, {
                  id: 'Identifier'
                }, {
                  id: 'ImpactLocation'
                }, {
                  id: 'Location'
                }, {
                  id: 'Resources'
                }, {
                  id: 'Measure'
                }]
            }]
        });
}

function updateScenarioPattern(id) {

    // get the selected location from the dropbox
    const location = document.getElementById('site').value;
    if (location == 'Location') {
         window.alert("Please select a location");
          $("#sen0").hide();
    }else{
        $("#sen0").show();
    }
    collectData(location);

    // fetch location specific data from the backend for defaults
    let ids =  getOutageIds(location, Infinity);
    let defaultId = ids[0];
    if (id === "undefined"){
        id = defaultId;
    }

    chart(CONTAINER_NAME, location, id);
}
