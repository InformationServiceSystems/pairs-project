var bubbleChart = null;
function getData(location){
    const url = 'http://127.0.0.1:8000/OutageForecast/predict/?city='+ location;
    fetch(url).then(response => {
        response.json().then(data=> {
            const predictions = data.Predictions;
            const confidence = data.Confidence;
            const features = data.Features;
            const data_org = data.Weather;
            console.log(location, confidence, predictions, features, data_org);
            const fullPopData = []
            for(let i = 0; i < confidence.length; i++) {
                const popData = [];
                for(let j = 0; j <= i; j++) {
                    popData.push({x: j + 1, y: (confidence[j] * 100).toFixed(2), r: 10, color: predictions[j] == 1 ? 'red' : 'green'})
                }
                fullPopData.push(popData);
            }
            predictionGraph(location, fullPopData[6]);
            updateScenarioPattern(0);


        });
    })
}


function predictionGraph(location, popData){
    var popCanvas = document.getElementById("popChart");

    Chart.defaults.global.defaultFontFamily = "sans-serif";
    Chart.defaults.global.defaultFontSize = 15
    if(bubbleChart !== null) {
        bubbleChart.destroy();
    }
    bubbleChart = new Chart(popCanvas, {
          type: 'bubble',
          events: ['click'],
          options : {
              tooltips:{
                callbacks:{
                   label: (context) =>{
                    return context.yLabel + "%";
                   }
                },
              },
              layout:{
                padding:20
              },
              onClick: function(e) {
                  const id = this.getElementsAtEvent(e)[0]["_index"];
                 // console.log("id ", id);
                  updateScenarioPattern(id);
              },
              responsive: true,
              maintainAspectRatio: false,
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
                    display: false,
                    labelString: 'Confidence level'
                  }
                }],
                x : {

               ticks: {
                          callback: function(val, index) {
                            return index % 2 === 0 ? this.getLabelForValue(val) : '';

                         }
                  }
                },
                xAxes: [{
                    ticks: {
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
                label: location,
                backgroundColor: popData.map(x => x.color),
                data: popData,

            }],
          }
    });

    //+++++set the optimun confidence level+++++++++++++
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


    //+++++++++++++Informations for users++++++++++
    var Outage_type = [];
     for(let i=0; i< popData.length; i++){
        Outage_type.push(popData[i].color);
     }

         if(!(Outage_type.includes("red"))){
              document.getElementById("place").innerHTML  = location;
              document.getElementById("marker_text").innerHTML  = "There will be <strong>no outage </strong> in <strong>" + location + "</strong> for the next <strong>" + 7 + " </strong> days"
              document.getElementById("btn1").style.background='green';
               $("#no_disruption").show();
               $("#load").hide();
               $("#disruption").hide();
            } else {
                document.getElementById("place").innerHTML  = location;
                for (let j=  0; j< popData.length; j++){
                    var confidence_level = popData[j].y;
                    console.log("confidence_level ", confidence_level);
                    if (popData[j].color == "red"){
                      var someDate = new Date();
                      var numberOfDaysToAdd = j +1;
                      var result = someDate.setDate(someDate.getDate() + numberOfDaysToAdd);
                      var today = new Date(result);
                      var dd = String(today.getDate()).padStart(2, '0');
                      var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
                      var yyyy = today.getFullYear();
                      today = dd + '.' + mm + '.' + yyyy;
                      var feedback_line = document.createElement('div');
                      feedback_line.innerHTML = "There will be <strong>an outage </strong> in <strong>" + location + "</strong> on <strong>" + today +"</strong> with a probablity of <strong>" + confidence_level + "%" + "</strong>";
                      document.getElementById('marker_text').append( feedback_line );
                    }
                    continue;
                }
                document.getElementById("btn1").style.background='red';
                $("#disruption").show();
                $("#no_disruption").hide();
                $("#load").hide();
            }

}


function onClick() {
    const location = document.getElementById('site').value;
    document.getElementById('marker_text').innerHTML = '';
    if(location !== 'Location')
        getData(location);

}


