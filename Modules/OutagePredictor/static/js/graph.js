
     //Tweeter Classification Chart
/*let ctx1 = document.getElementById("bar-chart-horizontal1").getContext('2d');
let ctx2 = document.getElementById("bar-chart-horizontal2").getContext('2d');
let ctx3 = document.getElementById("bar-chart-horizontal3").getContext('2d');
let ctx4 = document.getElementById("bar-chart-horizontal4").getContext('2d');
let ctx5 = document.getElementById("bar-chart-horizontal5").getContext('2d');
let ctx6 = document.getElementById("bar-chart-horizontal6").getContext('2d');
let ctx7 = document.getElementById("bar-chart-horizontal7").getContext('2d');

 var chart1 = new Chart(ctx1, {
                type: 'horizontalBar',
                data: {
                   labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [5,20,60,15]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart2 = new Chart(ctx2, {
                type: 'horizontalBar',
                data: {
                   labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [38,28,21,13]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart3 = new Chart(ctx3, {
                type: 'horizontalBar',
                data: {
                   labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",

                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [20,10,13,57]

                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart4 = new Chart(ctx4, {
                type: 'horizontalBar',
                data: {
                   labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data:[32,19,36,13]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart5 = new Chart(ctx5, {
                type: 'horizontalBar',
                data: {
                  labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [58,5,18,19]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart6 = new Chart(ctx6, {
                type: 'horizontalBar',
                data: {
                  labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [44,15,13,28]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                      scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });
var chart7 = new Chart(ctx7, {
                type: 'horizontalBar',
                data: {
                  labels: ["Stromausfall", "Wetter-bezogen", "Technisches Versagen", "nicht relevant"],
                  datasets: [
                    {
                      label: "Population (millions)",
                      backgroundColor: ["#3E95CD", "#8E5EA2","#3CBA9F","#E8C3B9"],
                      data: [35,31,24,10]
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                  },
                  scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 1,
                                    beginAtZero: true
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "white",
                                    fontSize: 10,
                                    stepSize: 25,
                                    beginAtZero: true
                                }
                            }],
                  }
                }
            });

 //************Figure for Google Map******************

                ko.bindingHandlers.maplace = {
                    init: function(element, valueAccessor, allBindings, viewModel, bindingContext) {

                var data = [{
                        lat: 48.02524,
                        lon: 12.55526,
                        title: 'Trostberg',
                        html: '<h4>Trostberg details</h3> <br> <h5>Day 1: No outage with a confidence of 93% <h5> <br> <h5> Day 2: No outage with a confidence of 92% </h5> <br><h5> Day 3: No outage with a confidence of 84% </h5> <br><h5> Day 4: Outage with a confidence of 89% </h5>  <br><h5> Day 5: No outage with a confidence of 85% </h5> <br><h5> Day 6: No outage with a confidence of 87% </h5>  <br><h5> Day 7: No outage with a confidence of 91% </h5>',
                        zoom: 8,
                        icon: 'http://www.google.com/mapfiles/markerA.png'
                    },{
                        lat: 47.765473,
                        lon: 12.079456,
                        title: 'Raubling',
                        html: '<h4>Raubling details</h3> <br> <h5>Day 1: No outage with a confidence of 82% <h5> <br> <h5> Day 2: No outage with a confidence of 88% </h5> <br><h5> Day 3: No outage with a confidence of 95% </h5> <br><h5> Day 4: Outage with a confidence of 74% </h5>  <br><h5> Day 5: No outage with a confidence of 91% </h5> <br><h5> Day 6: Outage with a confidence of 86% </h5>  <br><h5> Day 7: Outage with a confidence of 68% </h5>',
                        //show_infowindows: true
                    },
                    {
                        lat: 48.37054,
                        lon: 10.89779,
                        title: 'Augsburg',
                        html: '<h4>Ausgsburg details</h3> <br> <h5>Day 1: No outage with a confidence of 89% <h5> <br> <h5> Day 2: No outage with a confidence of 93% </h5> <br><h5> Day 3: No outage with a confidence of 91% </h5> <br><h5> Day 4: No outage with a confidence of 85% </h5>  <br><h5> Day 5: No outage with a confidence of 81% </h5> <br><h5> Day 6: No outage with a confidence of 83% </h5>  <br><h5> Day 7: No outage with a confidence of 85% </h5>',
                       // show_infowindows: true
                    },
                    {
                        lat: 48.56264,
                        lon: 11.26306,
                        title: 'Schrobenhausen',
                        html: '<h3>Schrobenhausen Data</h3>',
                       // show_infowindows: true
                    },
                    {
                        lat: 49.47712,
                        lon: 10.98867,
                        title: 'Fürth',
                        html: '<h3>Fürth Data</h3>',
                       // show_infowindows: true
                    },
                    {
                        lat: 49.03646,
                        lon: 12.99503,
                        title: 'Teisnach',
                        html: '<h3>Teisnach Data</h3>',
                       // show_infowindows: true
                    },
                    {
                        lat: 48.78061,
                        lon: 12.86904,
                        title: 'Plattling',
                        html: '<h3>Plattling, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 47.75058,
                        lon: 11.73845,
                        title: 'Gmund',
                        html: '<h3>Gmund, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 48.10448,
                        lon: 10.65398,
                        title: 'Ettringen',
                        html: '<h3>Ettringen, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 47.81502,
                        lon: 10.8943,
                        title: 'Schongau',
                        html: '<h3>Schongau, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 47.88302,
                        lon: 10.62597,
                        title: 'Kaufbeuren',
                        html: '<h3>Kaufbeuren, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 47.8213,
                        lon: 10.43871,
                        title: 'Günzach',
                        html: '<h3>Günzach, Data</h3>',
                        //show_infowindows: true
                    },
                    {
                        lat: 48.28284,
                        lon: 9.7265,
                        title: 'Ehingen',
                        html: '<h3>Ehingen, Data</h3>',
                        //show_infowindows: true
                    }


                ];

                $(function() {
                    new Maplace({
                        locations: data,
                        map_div: $(element),
                        start: 4,
                        view_all_text: 'Points of interest',
                        type: 'circle',
                        shared: {
                            zoom: 16,
                            html: '%index'
                        },
                        circleRadiusChanged: function(index, point, marker) {
                          $('#radiusInfo').text(
                            ' - point #' + (index+1) + ' size: ' + parseInt(marker.getRadius()) + 'mt.'
                          );
                        }
                    }).Load();
                });
                    }
                };

                var myViewModel = {
                    personName: ko.observable('Bob'),
                    personAge: ko.observable(123)
                };

                ko.applyBindings(myViewModel);

*/