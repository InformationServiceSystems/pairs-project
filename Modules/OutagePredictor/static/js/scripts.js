
 /*+++++++Script for Map graph : Scenario patent +++++++*/

     var celticColor1 = "#ed21c8",
     celticColor2 = "#f018c9",
     celticColor3 = "#e022be",
     italicColor1 = "#c91caa",
     italicColor2 = "#b51b99",
     italicColor3 = "#d420b3",
     //italicColor4 = "#ecb29b",
     indoIranianColor1 = "#ed28c9";
     indoIranianColor2 = "#d41eb2";
     indoIranianColor3 = "#cf23af";
     indoIranianColor4 = "#e82ac5";
     indoIranianColor5 = "#d138b5";
     indoIranianColor6 = "#c72aaa";
     indoIranianColor7 = "#c728aa";

/*++++++++++++++++Scenario pattern Raubling ++++++++++*/
Highcharts.chart('container', {
        chart: {
            type: 'networkgraph',
            marginTop: 35
        },
        title: {
            text: 'Scenario Pattern'
        },
         tooltip: {
                    formatter: function () {
              var info = "";
              switch (this.color) {
                case indoIranianColor2:
                  info = "<br><b>Postcondition:</b> machine downtime <br>  <b>Complexity:</b> Low" ;
                  break;
                case indoIranianColor3:
                  info = "<br><b>City:</b> Raubling <br>  <b>Region:</b> Bavaria";
                  break;
                case indoIranianColor4:
                  info = "<br><b>Identifier_ID:</b> Outage_431 <br>  <b>Timestamp:</b> 2022-07-18T13:38:56+0000";
                  break;
                case indoIranianColor5:
                  info = "<br><b>Precondition:</b> Thunderstorm <br>  <b>Probability:</b> 0.86";
                  break;
                case indoIranianColor6:
                  info = "<br><b>Organization:</b> [Bundesnetzagentur, NCEI] ";
                  break;
                case indoIranianColor7:
                  info = "<br><b>ScenarioDescription:</b> Outage based on shutdown windturbines, power grid fluctuation <br>  <b>Data:</b> wdsp,mxpsd,gust,4.0,7.0,26.6645... <br><b>InfluentialFactors:</b> weather conditions, heatwave, summer storms";
                  break;
                case celticColor1:
                  info = "<br><b>ActorRole:</b> Worker, Plan Manager <br>  <b>Skillset:</b> Maintenance work, Technical expertise";
                  break;
                case celticColor2:
                  info = "<br><b>Title:</b> Outage <br>  <b>ID:</b> Outage_431 <br> <b>Timestamp:</b> 2022-07-18T13:38:56+0000";
                  break;
                case celticColor3:
                  info = "<br><b>City:</b> Raubling <br>  <b>Region:</b> Bavaria";
                  break;
                 case italicColor1:
                  info = "<br><b>City:</b> Raubling <br>  <b>Region:</b> Bavaria";
                  break;
                case italicColor2:
                  info = "<br><b>Equipement:</b> None";
                  break;
                case italicColor3:
                  info = "<br><b>Actionstep:</b> Plan downtime, Plan maintenance, Controlled Shutdown <br>  <b>Category:</b> precautionary";
                  break;
              }
              return "<b>" + this.key + "</b>: " + info;
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
                ['Ressources', 'Location'],
                ['Measure', 'Ressources'],
                ['Actors', 'Measure']
                ],
            nodes: [{
                  id: 'Scenario',
                  color: indoIranianColor1
                }, {
                      id: 'Effect',
                  color: indoIranianColor2
                }, {
                  id: 'ScenarioLocation',
                  color: indoIranianColor3
                }, {
                  id: 'History',
                  color: indoIranianColor4
                }, {
                  id: 'Reason',
                  color: indoIranianColor5
                }, {
                  id: 'Source',
                  color: indoIranianColor6
                }, {
                  id: 'Context',
                  color: indoIranianColor7
                }, {
                  id: 'Actors',
                  color: celticColor1
                }, {
                  id: 'Identifier',
                  color: celticColor2
                }, {
                  id: 'ImpactLocation',
                  color: celticColor3
                }, {
                  id: 'Location',
                  color: italicColor1
                }, {
                  id: 'Ressources',
                  color: italicColor2
                }, {
                  id: 'Measure',
                  color: italicColor3
                }]
            }]
        });

/*++++++++++++++++Scenario pattern Torstberg ++++++++++*/
Highcharts.chart('container1', {
        chart: {
            type: 'networkgraph',
            marginTop: 35
        },
        title: {
            text: 'Scenario Pattern'
        },
         tooltip: {
                    formatter: function () {
              var info = "";
              switch (this.color) {
                case indoIranianColor2:
                  info = "<br><b>Postcondition:</b> machine downtime <br>  <b>Complexity:</b> Low" ;
                  break;
                case indoIranianColor3:
                  info = "<br><b>City:</b> Trostberg <br>  <b>Region:</b> Bavaria";
                  break;
                case indoIranianColor4:
                  info = "<br><b>Identifier_ID:</b> Outage_431, Outage_538";
                  break;
                case indoIranianColor5:
                  info = "<br><b>Precondition:</b> Thunderstorm <br>  <b>Probability:</b> 0.89";
                  break;
                case indoIranianColor6:
                  info = "<br><b>Organization:</b> Bundesnetzagentur, NCEI";
                  break;
                case indoIranianColor7:
                  info = "<br><b>ScenarioDescription:</b> Outage based on shutdown windturbines ; power grid fluctuation <br>  <b>Data:</b> wdsp,mxpsd,gust,4.0,7.0,26.6645... <br><b>InfluentialFactors:</b>weather conditions, heatwave, summer storms";
                  break;
                case celticColor1:
                  info = "<br><b>ActorRole:</b> Worker, Plan Manager <br>  <b>Skillset:</b> Maintenance work, Technical expertise";
                  break;
                case celticColor2:
                  info = "<br><b>Title:</b> Outage <br>  <b>ID:</b> Outage_874 <br> <b>Timestamp:</b> 2022-07-18T13:38:56+0000";
                  break;
                case celticColor3:
                  info = "<br><b>City:</b> Trostberg <br>  <b>Region:</b> Bavaria";
                  break;
                 case italicColor1:
                  info = "<br><b>City:</b> Trostberg <br>  <b>Region:</b> Bavaria";
                  break;
                case italicColor2:
                  info = "<br><b>Equipement:</b> None";
                  break;
                case italicColor3:
                  info = "<br><b>Actionstep:</b> Plan downtime, Plan maintenance, Controlled Shutdown <br>  <b>Category:</b> precautionary";
                  break;
              }
              return "<b>" + this.key + "</b>: " + info;
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
                ['Ressources', 'Location'],
                ['Measure', 'Ressources'],
                ['Actors', 'Measure']
                ],
            nodes: [{
                  id: 'Scenario',
                  color: indoIranianColor1
                }, {
                      id: 'Effect',
                  color: indoIranianColor2
                }, {
                  id: 'ScenarioLocation',
                  color: indoIranianColor3
                }, {
                  id: 'History',
                  color: indoIranianColor4
                }, {
                  id: 'Reason',
                  color: indoIranianColor5
                }, {
                  id: 'Source',
                  color: indoIranianColor6
                }, {
                  id: 'Context',
                  color: indoIranianColor7
                }, {
                  id: 'Actors',
                  color: celticColor1
                }, {
                  id: 'Identifier',
                  color: celticColor2
                }, {
                  id: 'ImpactLocation',
                  color: celticColor3
                }, {
                  id: 'Location',
                  color: italicColor1
                }, {
                  id: 'Ressources',
                  color: italicColor2
                }, {
                  id: 'Measure',
                  color: italicColor3
                }]
            }]
        });

/*++++++++++++++++Scenario pattern Augsburg ++++++++++*/
Highcharts.chart('container2', {
        chart: {
            type: 'networkgraph',
            marginTop: 35
        },
        title: {
            text: 'Scenario Pattern'
        },
         tooltip: {
                    formatter: function () {
              var info = "";
              switch (this.color) {
                case indoIranianColor2:
                  info = "<br><b>Postcondition:</b> machine downtime <br>  <b>Complexity:</b> Low" ;
                  break;
                case indoIranianColor3:
                  info = "<br><b>City:</b> Augsburg <br>  <b>Region:</b> Bavaria";
                  break;
                case indoIranianColor4:
                  info = "<br><b>Identifier_ID:</b> Outage_431";
                  break;
                case indoIranianColor5:
                  info = "<br><b>Precondition:</b> Thunderstorm <br>  <b>Probability:</b> 0.78";
                  break;
                case indoIranianColor6:
                  info = "<br><b>Organization:</b> Bundesnetzagentur, NCEI";
                  break;
                case indoIranianColor7:
                  info = "<br><b>ScenarioDescription:</b> Outage based on shutdown windturbines,  power grid fluctuation <br>  <b>Data:</b> wdsp,mxpsd,gust,4.0,7.0,26.6645... <br><b>InfluentialFactors:</b> weather conditions, heatwave, summer storms";
                  break;
                case celticColor1:
                  info = "<br><b>ActorRole:</b> Worker, Plan Manager <br>  <b>Skillset:</b> Maintenance work, Technical expertise";
                  break;
                case celticColor2:
                  info = "<br><b>Title:</b> Outage <br>  <b>ID:</b> Outage_538 <br> <b>Timestamp:</b> 2022-07-18T13:38:56+0000";
                  break;
                case celticColor3:
                  info = "<br><b>Region:</b> Bavaria";
                  break;
                 case italicColor1:
                  info = "<br><b>City:</b> Augsburg <br>  <b>Region:</b> Bavaria";
                  break;
                case italicColor2:
                  info = "<br><b>Equipement:</b> None";
                  break;
                case italicColor3:
                  info = "<br><b>Actionstep:</b> Plan downtime, Plan maintenance, Controlled Shutdown <br>  <b>Category:</b> precautionary";
                  break;
              }
              return "<b>" + this.key + "</b>: " + info;
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
                ['Ressources', 'Location'],
                ['Measure', 'Ressources'],
                ['Actors', 'Measure']
                ],
            nodes: [{
                  id: 'Scenario',
                  color: indoIranianColor1
                }, {
                      id: 'Effect',
                  color: indoIranianColor2
                }, {
                  id: 'ScenarioLocation',
                  color: indoIranianColor3
                }, {
                  id: 'History',
                  color: indoIranianColor4
                }, {
                  id: 'Reason',
                  color: indoIranianColor5
                }, {
                  id: 'Source',
                  color: indoIranianColor6
                }, {
                  id: 'Context',
                  color: indoIranianColor7
                }, {
                  id: 'Actors',
                  color: celticColor1
                }, {
                  id: 'Identifier',
                  color: celticColor2
                }, {
                  id: 'ImpactLocation',
                  color: celticColor3
                }, {
                  id: 'Location',
                  color: italicColor1
                }, {
                  id: 'Ressources',
                  color: italicColor2
                }, {
                  id: 'Measure',
                  color: italicColor3
                }]
            }]
        });
/*+++++++++++++++++++ende Senario Pattern++++++++++++++++++++++*/


//**********************Bubble Graph******************
            var popCanvas = document.getElementById("popChart");

                Chart.defaults.global.defaultFontFamily = "sans-serif";
                Chart.defaults.global.defaultFontSize = 15;

                //++++++++++Dynamic Graph
               /* var popData1 = [{x: 1,y: 82, r: 10 }];
                var popData2 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}];
                var popData3 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}];
                var popData4 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}];
                var popData5 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}];
                var popData6 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}, {x: 6,y: 86,r: 10}];
                var popData7 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}, {x: 6,y: 86,r: 10},{x: 7,y: 68,r: 10}]*/


                //Location Raubling data
                var popData1 = [{x: 1,y: 82, r: 10 }];
                var popData2 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}];
                var popData3 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}];
                var popData4 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}];
                var popData5 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}];
                var popData6 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}, {x: 6,y: 86,r: 10}];
                var popData7 = [{x: 1,y: 82, r: 10 }, {x: 2,y: 88,r: 10}, {x: 3,y: 95, r: 10}, {x: 4,y: 74,r: 10}, {x: 5,y: 91,r: 10}, {x: 6,y: 86,r: 10},{x: 7,y: 68,r: 10}]

                //Location Trostberg

                var popData12 = [{x: 1,y: 93, r: 10 }];
                var popData22 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}];
                var popData32 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}, {x: 3,y: 84, r: 10}];
                var popData42 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}, {x: 3,y: 84, r: 10}, {x: 4,y: 89,r: 10}];
                var popData52 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}, {x: 3,y: 84, r: 10}, {x: 4,y: 89,r: 10}, {x: 5,y: 85,r: 10}];
                var popData62 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}, {x: 3,y: 84, r: 10}, {x: 4,y: 89,r: 10}, {x: 5,y: 85,r: 10}, {x: 6,y: 87,r: 10}];
                var popData72 = [{x: 1,y: 93, r: 10 }, {x: 2,y: 92,r: 10}, {x: 3,y: 84, r: 10}, {x: 4,y: 89,r: 10}, {x: 5,y: 85,r: 10}, {x: 6,y: 87,r: 10},{x: 7,y: 91,r: 10}]


                //Location Augsburg
                var popData13 = [{x: 1,y: 89, r: 10 }];
                var popData23 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}];
                var popData33 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}, {x: 3,y: 91, r: 10}];
                var popData43 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}, {x: 3,y: 91, r: 10}, {x: 4,y: 85,r: 10}];
                var popData53 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}, {x: 3,y: 91, r: 10}, {x: 4,y: 85,r: 10}, {x: 5,y: 81,r: 10}];
                var popData63 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}, {x: 3,y: 91, r: 10}, {x: 4,y: 85,r: 10}, {x: 5,y: 81,r: 10}, {x: 6,y: 83,r: 10}];
                var popData73 = [{x: 1,y: 89, r: 10 }, {x: 2,y: 93,r: 10}, {x: 3,y: 91, r: 10}, {x: 4,y: 85,r: 10}, {x: 5,y: 81,r: 10}, {x: 6,y: 83,r: 10},{x: 7,y: 85,r: 10}];



                var bubbleChart = new Chart(popCanvas, {
                  type: 'bubble',

                  options : {
                      responsive: true,
                      maintainAspectRatio: false,
                      events: [],
                      title : {
                      display: false,
                        text:'Prediction of energy driven disruptions in upcoming 7 days',
                      },
                      lineAt: 80,
                      scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                stepSize: 20,
                            },
                          scaleLabel: {
                            display: true,
                            labelString: 'Confidence level'
                          }
                        }],
                        x : {

                       ticks: {

                                  // For a category axis, the val is the index so the lookup via getLabelForValue is needed
                                  callback: function(val, index) {
                                    // Hide the label of every 2nd dataset
                                    return index % 2 === 0 ? this.getLabelForValue(val) : '';

                                 }
                          }
                        },
                        xAxes: [{
                            ticks: {
                                //beginAtZero: true,
                                min:1,
                                stepSize: 1,
                                max:7
                            },
                          scaleLabel: {
                            display: true,
                            labelString: 'Days',

                          }
                        }]
                      },
                      legend:{
                          labels:{
                             boxWidth: 0,
                         }
                      }
                    },
                  data: {
                  datasets: [{
                        label: [],
                        backgroundColor: [],
                        //backgroundColor1: ["green","Green","Red","Green","Green","green", "green"],
                        data: [],
                        //data: [{x:0,y:0,r:0},{x:0,y:0,r:0},{x:0,y:0,r:0},{x:0,y:0,r:0},{x:0,y:0,r:0},{x:0,y:0,r:0},{x:0,y:0,r:0}],

                    }],
                }});

                const ctx = popCanvas.getContext('2d');
                Chart.pluginService.register({
                afterDraw: function(chart) {
                    if (typeof chart.config.options.lineAt != 'undefined') {
                       var lineAt = chart.config.options.lineAt;
                        var ctxPlugin = chart.chart.ctx;
                        var xAxe = chart.scales[chart.config.options.scales.xAxes[0].id];
                        var yAxe = chart.scales[chart.config.options.scales.yAxes[0].id];
                        if(yAxe.min != 0) return;
                        ctxPlugin.strokeStyle = "Orange";
                        ctxPlugin.beginPath();
                        lineAt = (lineAt - yAxe.min) * (100 / yAxe.max);
                        lineAt = (100 - lineAt) / 100 * (yAxe.height) + yAxe.top;
                        ctxPlugin.moveTo(xAxe.left, lineAt);
                        ctxPlugin.lineTo(xAxe.right, lineAt);
                        ctxPlugin.stroke();
                    }
                }
            });


                const fieldsetnew = document.querySelector('.fieldset');
                var form = fieldsetnew.querySelectorAll('#forme');
                submitInput = form[0].querySelector('input[type="submit"]');
                var collectedDatanew = [];
                var loc2;
                var time2=0;
                var popVar  = {"1":popData1,"2":popData2,"3":popData3,"4":popData4,"5":popData5,"6":popData6,"7":popData7};
                var popVar2  = {"1":popData12,"2":popData22,"3":popData32,"4":popData42,"5":popData52,"6":popData62,"7":popData72};
                var popVar3  = {"1":popData13,"2":popData23,"3":popData33,"4":popData43,"5":popData53,"6":popData63,"7":popData73};



//***************Let have a function for Update our Pages**************

    async function getDataForm(e){
        e.preventDefault();
       /* collectedData.splice(0, collectedData.length);
        var formData = new FormData(form[0]);
        collectedData.push(formData.get('site'));
        collectedData.push(formData.get('tentacles'));
        console.log(collectedData);
        loc = collectedData[0];
        time = collectedData[1];*/
        preds_raubling = [0,0,0,0,0,1,1]
        confidence_raubling = [82, 88, 95, 74, 91, 86, 68]

        preds_ausburg = [0,0,0,0,0,0,0]
        confidence_ausburg = [89, 93, 91, 85, 81, 83, 85]

        preds_trostberg = [0,0,0,1,0,0,0]
        confidence_trostberg = [93, 92, 84, 89, 85, 87, 91]




        //Data for the Bubble Graph
        collectedDatanew.splice(0, collectedDatanew.length);
        var formDatanew = new FormData(form[0]);
        collectedDatanew.push(formDatanew.get('site'));
        var tentacles = 7
        collectedDatanew.push(tentacles);
        console.log('collectedDatanew ' + collectedDatanew);
        loc2 = collectedDatanew[0];
        time2 = collectedDatanew[1];

        console.log("hier bin ich");

        //++++++++dynamic data inputs
        const url = 'http://127.0.0.1:8000/OutageForecast/predict/?city='+ loc2;
        var Arr = [];

        fetch(url).then(response => {
        response.json().then(data=> {
            const predictions = data.Predictions;
            const confidence = data.Confidence;
            console.log("confidence", confidence);
            console.log("confidence", confidence[1]);

        });
    })

       /* async function getISS(){
            const response = await fetch(url);
            const data = await response.json();

            console.log("data ", data);

            Arr.push(data.Predictions);
            Arr.push(data.Confidence);

             for(var i in result){
                resultat.push(result[i]);
            }

            }
       getISS();*/





        //++++ Update Twitter Infos
        console.log("time2 " + time2 );
        var forcasting_days = parseInt(time2);

        /*--Updating confidence and outage in the line below the graph---*/

        console.log("today: "+ today)

        preds_raubling = [0,0,0,0,0,1,1]
        confidence_raubling = [82, 88, 95, 74, 91, 86, 68]

        preds_ausburg = [0,0,0,0,0,0,0]
        confidence_ausburg = [89, 93, 91, 85, 81, 83, 85]

        preds_trostberg = [0,0,0,1,0,0,0]
        confidence_trostberg = [93, 92, 84, 89, 85, 87, 91]

        if(loc2=="Augsburg"){
          console.log("forecasting_Days " + forcasting_days)
          document.getElementById("marker_text").innerHTML  = "There will be <strong>no outage </strong> in <strong> Augsburg </strong> for the next <strong>" + forcasting_days + " </strong> days"
        }
        if(loc2=="Trostberg" & forcasting_days>3){
         
          var someDate = new Date();
          var numberOfDaysToAdd = 4;
          var result = someDate.setDate(someDate.getDate() + numberOfDaysToAdd);
          var today = new Date(result);
          var dd = String(today.getDate()).padStart(2, '0');
          var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
          var yyyy = today.getFullYear();
          today = dd + '.' + mm + '.' + yyyy;

           document.getElementById("marker_text").innerHTML  = "There will be <strong>an outage </strong> in <strong>Trostberg</strong> on <strong>" + today +"</strong> with a probablity of <strong>89% </strong>"
        }

        if(loc2=="Trostberg" & forcasting_days<=3){
         document.getElementById("marker_text").innerHTML  = "There will be <strong>no outage </strong> in <strong> Trostberg </strong> for the next <strong>" + forcasting_days + " </strong> days" 
        }

        if(loc2=="Raubling" & forcasting_days>5){
         
          var someDate = new Date();
          var numberOfDaysToAdd = 6;
          var result = someDate.setDate(someDate.getDate() + numberOfDaysToAdd);
          var today = new Date(result);
          var dd = String(today.getDate()).padStart(2, '0');
          var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
          var yyyy = today.getFullYear();
          today = dd + '.' + mm + '.' + yyyy;

           document.getElementById("marker_text").innerHTML  = "There will be <strong>an outage </strong> in <strong>Raubling</strong> on <strong>" + today +"</strong> with a probablity of <strong>86% </strong>" 
        }
        if(loc2=="Raubling" & forcasting_days<=5){
         document.getElementById("marker_text").innerHTML  = "There will be <strong>no outage </strong> in <strong> Raubling </strong> for the next <strong>" + forcasting_days + " </strong> days" 
        }


        h1 = document.getElementById("c1");
        h2 = document.getElementById("c2");
        h3 = document.getElementById("c3");
        h4 = document.getElementById("c4");
        h5 = document.getElementById("c5");
        h6 = document.getElementById("c6");
        h7 = document.getElementById("c7");


        if (loc2 == "Raubling"){
            bubbleChart.data.datasets[0].data = popVar[time2];
            bubbleChart.data.datasets[0].label = loc2;
            bubbleChart.data.datasets[0].backgroundColor = ["green","green","green","green","green","red", "red"];
            //bubbleChart.data.datasets[0].backgroundColor = ["green","green","green","green","green","green", "green"];
            console.log('hohoho' + bubbleChart.data.datasets[0].data);
            collectedDatanew= [];

            $("#jsn").show();
            $("#jsn2").hide();
            $("#jsn3").hide();

            $("#res1").hide();
            $("#neg").hide();
            $("#pos").hide();

            $("#container").show();
            $("#container1").hide();
            $("#container2").hide();

            if(time2 == 7){
            $("#pos").show();
            $("#neg").hide();
            document.getElementById("btn1").style.background='red';

            // +++++++Gif Management+++++++

            $("#im2").show();
            $("#im1").show();
            $("#im2").hide();
            $("#load").hide();
            $("#im3").hide();

            }
        }

        if (loc2 == "Trostberg"){
            bubbleChart.data.datasets[0].data = popVar2[time2];
            bubbleChart.data.datasets[0].label = loc2;
            bubbleChart.data.datasets[0].backgroundColor = ["green","green","green","red","green","green", "green"];

            console.log('hohoho' + bubbleChart.data.datasets[0].data);

            collectedDatanew= [];

            $("#jsn3").show();
            $("#jsn").hide();
            $("#jsn2").hide();

            $("#res1").hide();
            $("#neg").hide();
            $("#pos").hide();

            $("#container").hide();
            $("#container1").show();
            $("#container2").hide();

            if(time2 == 7){
            $("#neg").hide();
            $("#pos").show();
            document.getElementById("btn1").style.background='red';

            // ++++++++Gif Management+++++++++

            $("#im3").hide();
            $("#im2").hide();
            $("#im1").show();
            $("#load").hide();
            $("#im2").hide();
            }
        }
        if (loc2 == "Augsburg"){
            bubbleChart.data.datasets[0].data = popVar3[time2];
            bubbleChart.data.datasets[0].label = loc2;
            bubbleChart.data.datasets[0].backgroundColor = ["green","green","green","green","green","green", "green"];
            console.log('hohoho' + bubbleChart.data.datasets[0].data);
            collectedDatanew= [];
             $("#pos").hide();
            $("#neg").hide();
            $("#res1").show();
            $("#jsn").hide();
            $("#jsn3").hide();
            $("#jsn2").show();
            $("#container").hide();
            $("#container1").hide();
            $("#container2").show();

            document.getElementById("btn1").style.background='green';

            // ++++++++Gif Management+++++++++

            $("#im3").show();
            $("#im2").hide();
            $("#im1").hide();
            $("#load").hide();
            $("#im2").hide();
        }


        if (loc2 == "Location"){
            window.alert("Please select a location and a timestamp");
        }

       // console.log("loc ", loc);
       //console.log("time ", time);
        /* data_arr= [0,1,0,1];    //data: Output of the prediction
        time2 = parseInt(time2) ; // Update the timeframe
        data_arr_upd = data_arr.splice(0,time2); // Update the Graph Week input
        console.log("data_arr_upd" , data_arr_upd)
        chart.data.datasets[0].data = data_arr_upd;
        chart.data.datasets[1].data = data_arr_upd;
        chart.data.datasets[0].label = loc2;
        chart.data.datasets[1].label = loc2;
        console.log("datasets " , chart.data.datasets); */

          // +++++++++++++Let update Texts in Doc+++++++

/*        document.getElementById("nbwk").innerHTML  = time2; //Send Time in DP*/
        document.getElementById("place").innerHTML  = loc2; // Send location in DP
        //document.getElementById("loc").innerHTML  = loc2; // Send location for the JSON

        //********Update result*******
       /* if (loc2 == "Augsburg"){
        console.log("Loki ", loc2);
            $("#pos").hide();
            $("#neg").hide();
            $("#res1").show();
            $("#jsn").hide();
            $("#jsn3").hide();
            $("#jsn2").show();
            $("#container").hide();
            $("#container1").hide();
            $("#container2").hide();
            $("#containerx").show();

            document.getElementById("btn1").style.background='green';

            // ++++++++Gif Management+++++++++

            $("#im3").show();
            $("#im2").hide();
            $("#im1").hide();
            $("#load").hide();
            $("#im2").hide();

        }

        if(loc2 == "Trostberg"){

            $("#jsn3").show();
            $("#jsn").hide();
            $("#jsn2").hide();

            $("#res1").hide();
            $("#neg").hide();
            $("#pos").hide();

            $("#container").hide();
            $("#container1").show();
            $("#container2").hide();
            $("#containerx").hide();

            if(time2 == 7){
            $("#neg").hide();
            $("#pos").show();
            document.getElementById("btn1").style.background='red';

            // ++++++++Gif Management+++++++++

            $("#im3").hide();
            $("#im2").hide();
            $("#im1").show();
            $("#load").hide();
            $("#im2").hide();
            }
        }

        if(loc2 == "Raubling"){
            $("#jsn").show();
            $("#jsn2").hide();
            $("#jsn3").hide();

            $("#res1").hide();
            $("#neg").hide();
            $("#pos").hide();

            $("#container").show();
            $("#container1").hide();
            $("#container2").hide();
            $("#containerx").hide();

            if(time2 == 7){
            $("#pos").show();
            $("#neg").hide();
            document.getElementById("btn1").style.background='red';

            // +++++++Gif Management+++++++

            $("#im2").show();
            $("#im1").show();
            $("#im2").hide();
            $("#load").hide();
            $("#im3").hide();

            }
        }*/


        // Update of Data streams
        /*for (let i = 0; i< data_arr.length; i++){
            if(data_arr[i] == 0){
               document.getElementById("atd").innerHTML  = "Data streams by active sensors: 0.0%";
            } else {
                document.getElementById("atd").innerHTML  = "Data streams by active sensors: 100%";
            }
        }*/

          // +++++++++++++Let update colors+++++++

         /* console.log("time2 ", time2);
          if(time2 > 4){
          console.log("ich bin hier");
            //document.getElementById("btn8").style.background='red';
            document.getElementById("btn3").style.background='red';
            document.getElementById("btn2").style.background='#cecdcd';
            document.getElementById("btn1").style.background='#cecdcd';
            // ++++++++++Gif Management+++++++
            $("#im1").show();
            $("#im2").show();
            $("#im3").hide();
            $("#load").hide();
            $("#im2").hide();

          } else if (time2 <= 2) {
           // document.getElementById("btn8").style.background='green';
            document.getElementById("btn1").style.background='green';
            document.getElementById("btn2").style.background='#cecdcd';
            document.getElementById("btn3").style.background='#cecdcd';

            // ++++++++Gif Management+++++++++

            $("#im3").show();
            $("#im2").show();
            $("#im1").hide();
            $("#load").hide();
            $("#im2").hide();

          } else {
           // document.getElementById("btn8").style.background='orange';
            document.getElementById("btn2").style.background='orange';
            document.getElementById("btn1").style.background='#cecdcd';
            document.getElementById("btn3").style.background='#cecdcd';

            // +++++++Gif Management+++++++

            $("#im2").show();
            $("#im1").show();
            $("#im1").hide();
            $("#load").hide();
            $("#im3").hide();
          }*/

        //chart.update();
        bubbleChart.update();

    }

        document.addEventListener('DOMContentLoaded', function(){
        submitInput.addEventListener('click', getDataForm, false);
    }, false);

