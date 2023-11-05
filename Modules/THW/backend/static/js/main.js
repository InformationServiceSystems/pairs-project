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

  if(dataWeather = 'hardcoded') {
    switch (location) {

      case 'Aachen (Nordrhein-Westfalen)':

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
        </tr>`

      break;

    case "Bengel (Mosel)":
      tableRows += `
        <tr>
            <td>14/11/2023</td>
            <td>5.49</td>
            <td>3.09</td>
            <td>9.98</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Heavy Rain</td>
        </tr>
        <tr>
            <td>15/11/2023</td>
            <td>11.51</td>
            <td>2.46</td>
            <td>9.60</td>
            <td>Yes</td>
            <td>No</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>16/11/2023</td>
            <td>10.18</td>
            <td>1.49</td>
            <td>6.73</td>
            <td>No</td>
            <td>Yes</td>
            <td>-</td>
        </tr>
        <tr>
            <td>17/11/2023</td>
            <td>9.62</td>
            <td>1.08</td>
            <td>4.50</td>
            <td>No</td>
            <td>Yes</td>
            <td>-</td>
        </tr>
        <tr>
            <td>18/11/2023</td>
            <td>9.86</td>
            <td>3.68</td>
            <td>5.00</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>19/11/2023</td>
            <td>5.56</td>
            <td>1.71</td>
            <td>7.59</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>20/11/2023</td>
            <td>6.26</td>
            <td>2.14</td>
            <td>5.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
      `
      break;
    case "Cochem (Rhineland-Palatinate)":
      tableRows += `
        <tr>
            <td>14/11/2023</td>
            <td>5.79</td>
            <td>3.05</td>
            <td>9.98</td>
            <td>Yes</td>
            <td>No</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>15/11/2023</td>
            <td>12.11</td>
            <td>4.06</td>
            <td>9.60</td>
            <td>No</td>
            <td>No</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>16/11/2023</td>
            <td>9.18</td>
            <td>3.49</td>
            <td>8.73</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>17/11/2023</td>
            <td>9.62</td>
            <td>2.08</td>
            <td>4.50</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>18/11/2023</td>
            <td>7.86</td>
            <td>3.68</td>
            <td>5.00</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>19/11/2023</td>
            <td>1.56</td>
            <td>2.01</td>
            <td>7.59</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>20/11/2023</td>
            <td>4.26</td>
            <td>2.14</td>
            <td>5.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
      `
      break;
    case "Bernkastel-Kues (Rhineland-Palatinate)":
      tableRows += `
        <tr>
            <td>14/11/2023</td>
            <td>6.79</td>
            <td>3.75</td>
            <td>7.98</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Heavy Rain</td>
        </tr>
        <tr>
            <td>15/11/2023</td>
            <td>11.11</td>
            <td>2.06</td>
            <td>9.60</td>
            <td>No</td>
            <td>Yes</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>16/11/2023</td>
            <td>10.18</td>
            <td>3.43</td>
            <td>4.73</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>17/11/2023</td>
            <td>10.62</td>
            <td>2.42</td>
            <td>9.50</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>18/11/2023</td>
            <td>8.21</td>
            <td>2.48</td>
            <td>6.02</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>19/11/2023</td>
            <td>1.56</td>
            <td>2.01</td>
            <td>3.59</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>20/11/2023</td>
            <td>4.26</td>
            <td>2.14</td>
            <td>8.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
      `
      break;
    case "Mülheim (Mosel)":
      tableRows += `
        <tr>
            <td>14/11/2023</td>
            <td>6.19</td>
            <td>2.87</td>
            <td>4.98</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>15/11/2023</td>
            <td>8.11</td>
            <td>2.06</td>
            <td>9.60</td>
            <td>No</td>
            <td>No</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>16/11/2023</td>
            <td>10.18</td>
            <td>2.12</td>
            <td>6.73</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>17/11/2023</td>
            <td>9.62</td>
            <td>1.42</td>
            <td>9.50</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>18/11/2023</td>
            <td>8.21</td>
            <td>2.18</td>
            <td>6.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>19/11/2023</td>
            <td>3.16</td>
            <td>2.01</td>
            <td>3.59</td>
            <td>Yes</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>20/11/2023</td>
            <td>4.26</td>
            <td>3.14</td>
            <td>5.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
      `
      break;
    case "Zell (Mosel)":
      tableRows += `
        <tr>
            <td>14/11/2023</td>
            <td>6.52</td>
            <td>4.17</td>
            <td>4.18</td>
            <td>Yes</td>
            <td>Yes</td>
            <td>Heavy Rain</td>
        </tr>
        <tr>
            <td>15/11/2023</td>
            <td>10.52</td>
            <td>2.06</td>
            <td>7.60</td>
            <td>No</td>
            <td>No</td>
            <td>Flood</td>
        </tr>
        <tr>
            <td>16/11/2023</td>
            <td>10.31</td>
            <td>2.12</td>
            <td>6.73</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>17/11/2023</td>
            <td>10.12</td>
            <td>2.12</td>
            <td>8.23</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>18/11/2023</td>
            <td>9.81</td>
            <td>2.58</td>
            <td>7.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>19/11/2023</td>
            <td>4.16</td>
            <td>2.41</td>
            <td>6.59</td>
            <td>Yes</td>
            <td>No</td>
            <td>-</td>
        </tr>
        <tr>
            <td>20/11/2023</td>
            <td>5.22</td>
            <td>2.34</td>
            <td>6.62</td>
            <td>No</td>
            <td>No</td>
            <td>-</td>
        </tr>
      `
      break;

    }

  }else{

    // Not Hardcoded cases
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