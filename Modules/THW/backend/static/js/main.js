// Create the content for the popup
var currentDate = new Date();

// Create an array to store the next 7 days
var nextSevenDays = [];

// Loop to generate the next 7 days
for (var i = 0; i < 7; i++) {
    // Get the date for the current iteration
    var nextDay = new Date(currentDate.getTime() + (i + 1) * 24 * 60 * 60 * 1000);

    // Extract the day, month, and year
    var day = nextDay.getDate();
    var month = nextDay.getMonth() + 1; // Months are zero-based
    var year = nextDay.getFullYear();

    // Format the date as "day/month/year"
    var formattedDate = day + '/' + month + '/' + year;
    // Add the formatted date to the array
    nextSevenDays.push(formattedDate);
}

function generateTableRows(dataWeather, location) {
    var tableRows = ``;

    if(location != 'Aachen (Nordrhein-Westfalen)'){

        for (var i = 0; i < 7; i++) {
            tableRows += `<tr>
              <td>` + nextSevenDays[i] + `</td>
              <td>${((dataWeather[i].temp - 32) / 1.8).toFixed(2)}</td>
              <td>${(dataWeather[i].wdsp * 0.514444).toFixed(2)}</td>
              <td>${(dataWeather[i].visib * 1.60934).toFixed(2)}</td>
              <td>${(dataWeather[i].rain_drizzle === 0) ? "No" : "Yes"}</td>
              <td>${(dataWeather[i].thunder === 0) ? "No" : "Yes"}</td>
              <td>${dataWeather[i].Event}</td>
            </tr>`;
        }

    }else{
        //Constant values as demonstration
        tableRows += `
            <tr>
                <td>2/7/2023</td>
                <td>21.49</td>
                <td>1.09</td>
                <td>9.98</td>
                <td>No</td>
                <td>No</td>
                <td>-</td>
            </tr>
            <tr>
                <td>3/7/2023</td>
                <td>21.51</td>
                <td>1.46</td>
                <td>9.60</td>
                <td>No</td>
                <td>No</td>
                <td>-</td>
            </tr>
            <tr>
                <td>4/7/2023</td>
                <td>22.18</td>
                <td>1.49</td>
                <td>6.73</td>
                <td>No</td>
                <td>Yes</td>
                <td>Heavy Rain</td>
            </tr>
            <tr>
                <td>5/7/2023</td>
                <td>21.62</td>
                <td>1.08</td>
                <td>4.50</td>
                <td>No</td>
                <td>Yes</td>
                <td>-</td>
            </tr>
            <tr>
                <td>6/7/2023</td>
                <td>21.86</td>
                <td>3.68</td>
                <td>5.00</td>
                <td>No</td>
                <td>No</td>
                <td>-</td>
            </tr>
            <tr>
                <td>7/7/2023</td>
                <td>20.56</td>
                <td>1.71</td>
                <td>7.59</td>
                <td>No</td>
                <td>No</td>
                <td>-</td>
            </tr>
            <tr>
                <td>8/7/2023</td>
                <td>19.26</td>
                <td>2.14</td>
                <td>5.62</td>
                <td>No</td>
                <td>No</td>
                <td>-</td>
            </tr>
        `
    }
    
    var popupTitle = `<h2 style="font-size: 16px;text-align: center;">${location}</h2>`
    
    return  popupTitle +`
      <table>
        <thead>
          <tr>
            <th></th>
            <th>Temperature, C&deg;</th>
            <th>Windspeed, m/s</th>
            <th>Visibility, km</th>
            <th>Drizzle</th>
            <th>Thunder</th>
            <th>Event</th>
          </tr>
        </thead>
        <tbody>
          `+tableRows+`
        </tbody>
      </table>
    `;
  }