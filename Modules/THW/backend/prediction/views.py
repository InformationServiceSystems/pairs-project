from django.shortcuts import render
from django.http import HttpResponse
import json


from io import BytesIO
import base64

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg'
import matplotlib.pyplot as plt

from django.shortcuts import render

# GET DATA
df = pd.read_excel("missiontask_with_units.xlsx")
df_withonout_nan=df.dropna()


# Create views here
def home_view(request, *args, **kwargs):

    # get_weather_biberach, plot_flood_prediction_biberach, plot_heavy_rain_prediction_biberach, plot_others_prediction_biberach, plot_snow_prediction_biberach = event_prediction('Biberach','Baden-Württemberg')
    # get_weather_goettingen, plot_flood_prediction_goettingen, plot_heavy_rain_prediction_goettingen, plot_others_prediction_goettingen, plot_snow_prediction_goettingen = event_prediction('Göttingen', 'Niedersachsen')
    # get_weather_trier, plot_flood_prediction_trier, plot_heavy_rain_prediction_trier, plot_others_prediction_trier, plot_snow_prediction_trier = event_prediction('Trier', 'Rheinland-Pfalz')
    # get_weather_augsburg, plot_flood_prediction_augsburg, plot_heavy_rain_prediction_augsburg, plot_others_prediction_augsburg, plot_snow_prediction_augsburg = event_prediction('Augsburg', 'Bavaria')
    # get_weather_regensburg, plot_flood_prediction_regensburg, plot_heavy_rain_prediction_regensburg, plot_others_prediction_regensburg, plot_snow_prediction_regensburg = event_prediction('Regensburg', 'Bavaria')
    # get_weather_chemnitz, plot_flood_prediction_chemnitz, plot_heavy_rain_prediction_chemnitz, plot_others_prediction_chemnitz, plot_snow_prediction_chemnitz = event_prediction('Chemnitz', 'Sachsen')
    # get_weather_neubrandenburg, plot_flood_prediction_neubrandenburg, plot_heavy_rain_prediction_neubrandenburg, plot_others_prediction_neubrandenburg, plot_snow_prediction_neubrandenburg = event_prediction('Neubrandenburg', 'Mecklenburg-Vorpommern')
    # get_weather_schwerin, plot_flood_prediction_schwerin, plot_heavy_rain_prediction_schwerin, plot_others_prediction_schwerin, plot_snow_prediction_schwerin = event_prediction('Schwerin', 'Mecklenburg-Vorpommern')
    get_weather_kiel, plot_flood_prediction_kiel, plot_heavy_rain_prediction_kiel, plot_others_prediction_kiel, plot_snow_prediction_kiel = event_prediction('Kiel', 'Schleswig-Holstein')

    return render(request, 'home.html', {
                                        # PLOTS in OVERVIEW
                                        # 'plot_requester_dutyHours': plot_requester_dutyHours(),
                                        # 'plot_requester_helperss': plot_requester_helperss(),
                                        # 'plot_dutyHours_missionTask': plot_dutyHours_missionTask(),
                                        # 'plot_helpers_missionTask': plot_helpers_missionTask(),
                                        # 'plot_dutyHours_typeOfService': plot_dutyHours_typeOfService(),
                                        # 'plot_helpers_typeOfService': plot_helpers_typeOfService(),

                                        # TABLE in OVERVIEW
                                        'df_withonout_nan_custom':get_data(),

                                        # KNOWLADGE GRAPH
                                        # 'graph_template': show_graph_database("Complete"),

                                        # PLOTS for PREDICTIONS of FLOOD
                                        # 'plot_flood_prediction_goettingen': plot_flood_prediction_goettingen,
                                        # 'plot_flood_prediction_biberach': plot_flood_prediction_biberach,
                                        # 'plot_flood_prediction_trier': plot_flood_prediction_trier,
                                        # 'plot_flood_prediction_augsburg': plot_flood_prediction_augsburg,
                                        # 'plot_flood_prediction_regensburg': plot_flood_prediction_regensburg,
                                        #'plot_flood_prediction_chemnitz': plot_flood_prediction_chemnitz,
                                        # 'plot_flood_prediction_neubrandenburg': plot_flood_prediction_neubrandenburg,
                                        # 'plot_flood_prediction_schwerin': plot_flood_prediction_schwerin,
                                        'plot_flood_prediction_kiel': plot_flood_prediction_kiel,
                                        # PLOTS for PREDICTIONS of HEAVY RAIN
                                        # 'plot_heavy_rain_prediction_goettingen': plot_heavy_rain_prediction_goettingen,
                                        # 'plot_heavy_rain_prediction_biberach':plot_heavy_rain_prediction_biberach,
                                        # 'plot_heavy_rain_prediction_trier':plot_heavy_rain_prediction_trier,
                                        # 'plot_heavy_rain_prediction_augsburg':plot_heavy_rain_prediction_augsburg,
                                        # 'plot_heavy_rain_prediction_regensburg':plot_heavy_rain_prediction_regensburg,
                                        # 'plot_heavy_rain_prediction_chemnitz':plot_heavy_rain_prediction_chemnitz,
                                        # 'plot_heavy_rain_prediction_neubrandenburg':plot_heavy_rain_prediction_neubrandenburg,
                                        # 'plot_heavy_rain_prediction_schwerin':plot_heavy_rain_prediction_schwerin,
                                        'plot_heavy_rain_prediction_kiel':plot_heavy_rain_prediction_kiel,
                                        # PLOTS for PREDICTIONS of OTHER
                                        # 'plot_others_prediction_goettingen': plot_others_prediction_goettingen,
                                        # 'plot_others_prediction_biberach': plot_others_prediction_biberach,
                                        # 'plot_others_prediction_trier': plot_others_prediction_trier,
                                        # 'plot_others_prediction_augsburg': plot_others_prediction_augsburg,
                                        # 'plot_others_prediction_regensburg': plot_others_prediction_regensburg,
                                        # 'plot_others_prediction_chemnitz': plot_others_prediction_chemnitz,
                                        # 'plot_others_prediction_neubrandenburg': plot_others_prediction_neubrandenburg,
                                        # 'plot_others_prediction_schwerin': plot_others_prediction_schwerin,
                                        'plot_others_prediction_kiel': plot_others_prediction_kiel,
                                        # PLOTS for PREDICTIONS of SNOW
                                        # 'plot_snow_prediction_goettingen': plot_snow_prediction_goettingen,
                                        # 'plot_snow_prediction_biberach': plot_snow_prediction_biberach,
                                        # 'plot_snow_prediction_trier': plot_snow_prediction_trier,
                                        # 'plot_snow_prediction_augsburg': plot_snow_prediction_augsburg,
                                        # 'plot_snow_prediction_regensburg': plot_snow_prediction_regensburg,
                                        # 'plot_snow_prediction_chemnitz': plot_snow_prediction_chemnitz,
                                        # 'plot_snow_prediction_neubrandenburg': plot_snow_prediction_neubrandenburg,
                                        # 'plot_snow_prediction_schwerin': plot_snow_prediction_schwerin,
                                        'plot_snow_prediction_kiel': plot_snow_prediction_kiel,

                                        #EMPTY PLOT
                                        'empty_plot': empty_plot(),

                                        # POPUP TABLES with WEATHER DATA
                                        # 'get_weather_biberach':get_weather_biberach,
                                        # 'get_weather_goettingen': get_weather_goettingen,
                                        # 'get_weather_trier': get_weather_trier,
                                        # 'get_weather_augsburg': get_weather_augsburg,
                                        # 'get_weather_regensburg': get_weather_regensburg,
                                        # 'get_weather_chemnitz': get_weather_chemnitz,
                                        # 'get_weather_neubrandenburg': get_weather_neubrandenburg,
                                        # 'get_weather_schwerin': get_weather_schwerin,
                                        'get_weather_kiel': get_weather_kiel,

                                        #RECOMMENDATIONS
                                        # 'graph_strong_rain': show_graph_database("Starkregen"),
                                        # 'graph_flood': show_graph_database("Hochwasser"),
                                        'getFloodBekJson': getFloodBekJson(),
                                        'getStarkregenFuehrJson': getStarkregenFiehrJson(),
                                        'getFloodOrdJson': getFloodOrdJson(),
                                        'getStarkregenBekJson': getStarkregenBekJson(),
                                        })

def event_prediction(city, state):
    import requests
    import numpy as np
    from joblib import load
    import xgboost as xgb
    import pandas as pd
    from geopy.geocoders import Nominatim
    import json
    import datetime

    states = {
        'Federal State_Baden-Württemberg': 0,
        'Federal State_Bayern': 0,
        'Federal State_Berlin': 0,
        'Federal State_Brandenburg': 0,
        'Federal State_Bremen': 0,
        'Federal State_Hamburg': 0,
        'Federal State_Hessen': 0,
        'Federal State_Mecklenburg-Vorpommern': 0,
        'Federal State_Niedersachsen': 0,
        'Federal State_Nordrhein-Westfalen': 0,
        'Federal State_Rheinland-Pfalz': 0,
        'Federal State_Saarland': 0,
        'Federal State_Sachsen': 0,
        'Federal State_Sachsen-Anhalt': 0,
        'Federal State_Schleswig-Holstein': 0,
        'Federal State_Thüringen': 0
    }

    if state == 'Baden-Württemberg':
        states['Federal State_Baden-Württemberg'] = 1
    elif state == 'Bayern':
        states['Federal State_Bayern'] = 1
    elif state == 'Berlin':
        states['Federal State_Berlin'] = 1
    elif state == 'Brandenburg':
        states['Federal State_Brandenburg'] = 1
    elif state == 'Bremen':
        states['Federal State_Bremen'] = 1
    elif state == 'Hamburg':
        states['Federal State_Hamburg'] = 1
    elif state == 'Hessen':
        states['Federal State_Hessen'] = 1
    elif state == 'Mecklenburg-Vorpommern':
        states['Federal State_Mecklenburg-Vorpommern'] = 1
    elif state == 'Niedersachsen':
        states['Federal State_Niedersachsen'] = 1
    elif state == 'Nordrhein-Westfalen':
        states['Federal State_Nordrhein-Westfalen'] = 1
    elif state == 'Rheinland-Pfalz':
        states['Federal State_Rheinland-Pfalz'] = 1
    elif state == 'Saarland':
        states['Federal State_Saarland'] = 1
    elif state == 'Sachsen':
        states['Federal State_Sachsen'] = 1
    elif state == 'Sachsen-Anhalt':
        states['Federal State_Sachsen-Anhalt'] = 1
    elif state == 'Schleswig-Holstein':
        states['Federal State_Schleswig-Holstein'] = 1
    elif state == 'Thüringen':
        states['Federal State_Thüringen'] = 1
    #

    my_list = list(states.values())

    # if city == 'Biberach' and state == 'Baden-Württemberg':
    #     lat, long = (48.339971, 8.032849)
    #     print("city:", city)
    #     print(lat, long)
    # else:
    print("city:", city + ', '+ state)
    # Get city location
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city, addressdetails=True)
    lat, long = location.latitude, location.longitude
    print(lat, long)

    #  Weather API
    url11 = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=cloudcover_low,weathercode,windspeed_10m,temperature_2m,pressure_msl,dewpoint_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,weathercode,windspeed_10m_max,windgusts_10m_max&temperature_unit=fahrenheit&current_weather=true&windspeed_unit=kn&precipitation_unit=inch&timezone=CET'.format(lat, long)
    res = requests.get(url11)
    res = res.json()

    # Pressure
    press = (res["hourly"]["pressure_msl"])
    daily_slp = []

    num = 7
    try:
        for i in range(7):
            daily_slp.append(np.array(press[24*(i):24*(i+1)]).mean())
    except Exception:
        num = 6

    #  Temprature!!!!!!!!!!
    temp = res["hourly"]["temperature_2m"]
    daily_temp = []
    for i in range(num):
        daily_temp.append(np.array(temp[24*(i):24*(i+1)]).mean())

    # Dewpoint
    dewp = res["hourly"]["dewpoint_2m"]
    daily_dewp = []
    for i in range(num):
        daily_dewp.append(np.array(dewp[24*(i):24*(i+1)]).mean())

    # Windspeed!!!!!!!!!!!
    wspd = res["hourly"]["windspeed_10m"]
    daily_wspd = []
    for i in range(num):
        daily_wspd.append(np.array(wspd[24*(i):24*(i+1)]).mean())

    # Cloudcover!!!!!!!!!!!!!!
    cldcover = res["hourly"]["cloudcover_low"]
    daily_visibility = []
    vals = []
    for i in range(num):
        val = 100 - (np.array(cldcover[24*(i):24*(i+1)]).mean())
        vals.append(val)
        new_value = ( (val - 0) / (100 - 0) ) * (6.20 - 0.6) + 0.6
        daily_visibility.append(new_value)

    # Weathercode
    wcode = res["hourly"]["weathercode"]

    # Fog
    daily_fog_indicator = []
    fog_codes = [45, 48]
    for i in range(num):
        daily_fog_indicator.append(any(item in fog_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Drizzle!!!!!!!!!!!!!!!!!!
    drizzle_codes = [51, 53, 55, 56, 57]
    daily_drizzle_indicator = []
    for i in range(num):
        daily_drizzle_indicator.append(any(item in drizzle_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Snow
    snow_codes = [71, 73, 75, 77]
    daily_snow_indicator = []
    for i in range(num):
        daily_snow_indicator.append(any(item in snow_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Thunder!!!!!!!!!!!!!!
    thunder_codes = [95, 96, 99]
    daily_thunder_indicator = []
    for i in range(num):
        daily_thunder_indicator.append(any(item in thunder_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    #  !!!!!!!!!!!
    daily_max_wspd = res["daily"]["windspeed_10m_max"]

    daily_max_wgust = res["daily"]["windgusts_10m_max"]

    daily_max_temp = res["daily"]["temperature_2m_max"]

    daily_min_temp = res["daily"]["temperature_2m_min"]

    daily_prcp = res["daily"]["precipitation_sum"]

    # SEASONS
    # Define the mapping of months to seasons in Germany
    season_mapping = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter'
    }

    # Get the current date
    current_date = datetime.datetime.now().date()

    # Calculate the forecast day (e.g., 3 days from today)
    current_date1 = current_date + datetime.timedelta(days=3)

    forecast_month = []
    for i in range(1,8):
        forecast_month.append((current_date + datetime.timedelta(days=i)).month)

    # Map the months to seasons
    forecast_seasons = [season_mapping[month] for month in forecast_month]

    # Convert seasons to numerical representations
    season_mapping_numerical = {
        'Winter': 1,
        'Spring': 2,
        'Summer': 3,
        'Autumn': 4
    }

    forecast_numerical = [season_mapping_numerical[season] for season in forecast_seasons]


    season_forecast = []

    for i in forecast_numerical:
        season_dict = {
            'season_Autumn' : 0,
            'season_Spring' : 0,
            'season_Summer' : 0,
            'season_Winter' : 0
        }
        if i == 1:
            season_dict['season_Winter'] = 1
        elif i == 2:
            season_dict['season_Spring'] = 1
        elif i == 3:
            season_dict['season_Summer'] = 1
        else:
            season_dict['season_Autumn'] = 1

        my_list_seasons = list(season_dict.values())
        season_forecast.append(my_list_seasons)


    season_list = season_forecast

    # All days weather
    days_weather = []
    for i in range (num):
        days_weather.append(np.array([daily_temp[i], daily_dewp[i], daily_slp[i], 996.125888, daily_visibility[i], daily_wspd[i], daily_max_wspd[i], daily_max_wgust[i], daily_max_temp[i], daily_min_temp[i], daily_prcp[i], int(daily_fog_indicator[i]), int(daily_drizzle_indicator[i]), int(daily_snow_indicator[i]), int(daily_thunder_indicator[i])] + season_list[i] + my_list))

    if num == 6:
        days_weather.append(days_weather[5])

    data = days_weather
    print('--------------------=======================------------------')

    #open weather API
    url2 = 'https://api.openweathermap.org/data/2.5/forecast/daily?lat='+str(lat)+'&lon='+str(long)+'&appid=088271b7435257185a8ccf9522df10ab&units=imperial'
    res12 = requests.get(url2)
    res2 = res12.json()

    pressure = []
    temperature = []
    for i in range(len(res2['list'])):
        pressure.append(res2['list'][i]['pressure'])

        temperature.append((res2['list'][i]['temp']['day'] + res2['list'][i]['temp']['min'] + res2['list'][i]['temp']['max'] + res2['list'][i]['temp']['night'] +  res2['list'][i]['temp']['eve'] + res2['list'][i]['temp']['morn'])/6)

    features_names = ['temp', 'dewp','slp', 'stp', 'visib', 'wdsp', 'mxpsd', 'gust', 'max', 'min', 'prcp','fog', 'rain_drizzle', 'snow_ice_pellets', 'thunder', 'season_Autumn', 'season_Spring','season_Summer', 'season_Winter', 'Federal State_Baden-Württemberg','Federal State_Bayern', 'Federal State_Berlin','Federal State_Brandenburg', 'Federal State_Bremen','Federal State_Hamburg', 'Federal State_Hessen','Federal State_Mecklenburg-Vorpommern', 'Federal State_Niedersachsen', 'Federal State_Nordrhein-Westfalen', 'Federal State_Rheinland-Pfalz','Federal State_Saarland', 'Federal State_Sachsen','Federal State_Sachsen-Anhalt', 'Federal State_Schleswig-Holstein','Federal State_Thüringen']

    # Load model
    model = xgb.XGBClassifier()
    model.load_model("model_option2_rfso.json")

    X_valid = pd.DataFrame(data, columns=features_names)
    X_valid['temp'] = temperature

    prob = model.predict_proba(X_valid)
    rounded_prob = np.round(prob, decimals=3)
    print(rounded_prob)

    target_value = 0.85

    found_array_indices = []
    found_value_indices = []
    event = []

    for i in range(len(rounded_prob)):
        current_array = rounded_prob[i]
        if np.any(current_array >= target_value):
            found_array_indices.append(i)
            found_value_indices.append(np.argmax(current_array))
            if(np.argmax(current_array) == 0):
                event.append('Flood')
            elif(np.argmax(current_array) == 1):
                event.append('Heavy Rain')
            elif(np.argmax(current_array) == 2):
                event.append('Others')
            elif(np.argmax(current_array) == 3):
                event.append('Snow')
        else:
            event.append('-')

    print("City:", city)
    print("Found Event:", event)
    print("Found Day Indices:", found_array_indices)
    print("Found Event Indices:", found_value_indices)

    # OUTPUT
    X_valid['Event'] = event
    json_data = X_valid.to_json(orient='records')

    plot_flood_prediction = flood_predinction(rounded_prob)
    plot_heavy_rain_prediction = heavy_rain_predinction(rounded_prob)
    plot_others_prediction = others_predinction(rounded_prob)
    plot_snow_prediction = snow_predinction(rounded_prob)

    # Convert rounded probabilities to JSON
    #rounded_prob_json = json.dumps(rounded_prob.tolist())
    return json_data, plot_flood_prediction, plot_heavy_rain_prediction, plot_others_prediction,plot_snow_prediction

#############################MODEL###############################
def getFloodBekJson():
    with open('static/js/FloodRecommendationBek.json', encoding='utf-8') as f:
        json_data = json.load(f)
    return json.dumps(json_data, ensure_ascii=False)

def getStarkregenFiehrJson():
    with open('static/js/RainRecommendationFuehr.json', encoding='utf-8') as f:
        json_data = json.load(f)
    return json.dumps(json_data, ensure_ascii=False)

def getFloodOrdJson():
    with open('static/js/FloodRecommendationOrd.json', encoding='utf-8') as f:
        json_data = json.load(f)
    return json.dumps(json_data, ensure_ascii=False)

def getStarkregenBekJson():
    with open('static/js/RainRecommendationBek.json', encoding='utf-8') as f:
        json_data = json.load(f)
    return json.dumps(json_data, ensure_ascii=False)

def flood_predinction(predictions):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.now().date()

    # Create an empty array to store the next seven days
    next_seven_days = []

    # Iterate over the range of next seven days and add them to the array
    for i in range(7):
        next_day = current_date + timedelta(days=i+1)
        formatted_date = next_day.strftime("%d/%m/%Y")
        next_seven_days.append(formatted_date)
    #

    pred_no_flood_x = []
    pred_flood_x = []
    pred_no_flood_y = []
    pred_flood_y = []
    for i in range(len(predictions)):
        num = i+1
        if predictions[i][0] <= 0.85:
            pred_no_flood_x.append(num)
            pred_no_flood_y.append(predictions[i][0]*100)
        elif predictions[i][0] > 0.85:
            pred_flood_x.append(num)
            pred_flood_y.append(predictions[i][0]*100)
        #
    #

    threshold = 85

    image_width_px = 1000
    dpi = 100  # Adjust the DPI value as needed
    inches_per_pixel = 1 / dpi
    width_inches = image_width_px * inches_per_pixel
    height_inches = width_inches * 0.6  # Adjust the height ratio as needed

    # Plotting
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 110)

    # Grid lines
    ax.grid(True, linestyle='--', alpha=0.5)

    # Scatter plot

    ax.scatter(pred_no_flood_x, pred_no_flood_y, color='green', s=700, label='No Flood Event')
    ax.scatter(pred_flood_x, pred_flood_y, color='red', s=700, label='Potential Flood Event')

    # Threshold line
    ax.plot([0, 8], [threshold, threshold], color='orange', linestyle='--', label='Threshold')

    # Axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Confidence')

    # Ticks
    ax.set_xticks(np.arange(1, 8))
    ax.set_xticklabels(next_seven_days, fontsize=9)
    ax.set_yticks(np.arange(0, 111, 20))

    # Legend
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1) ,borderpad=2,labelspacing=2)

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save plot as image file
    # if(city == 'Aachen'):
    #     filename = 'plot_flood_prediction_aachen.svg'  # Specify the filename and extension
    #     plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_flood_prediction = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_flood_prediction
#

def empty_plot():
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.now().date()

    # Create an empty array to store the next seven days
    next_seven_days = []

    # Iterate over the range of next seven days and add them to the array
    for i in range(7):
        next_day = current_date + timedelta(days=i + 1)
        formatted_date = next_day.strftime("%d/%m/%Y")
        next_seven_days.append(formatted_date)

    threshold = 85

    image_width_px = 1000
    dpi = 100  # Adjust the DPI value as needed
    inches_per_pixel = 1 / dpi
    width_inches = image_width_px * inches_per_pixel
    height_inches = width_inches * 0.6  # Adjust the height ratio as needed

    # Plotting
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 110)

    # Grid lines
    ax.grid(True, linestyle='--', alpha=0.5)

    # Threshold line
    ax.plot([0, 8], [threshold, threshold], color='orange', linestyle='--', label='Threshold')

    # Axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Confidence')

    # Ticks
    ax.set_xticks(np.arange(1, 8))
    ax.set_xticklabels(next_seven_days, fontsize=9)
    ax.set_yticks(np.arange(0, 111, 20))

    # Legend
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), borderpad=2, labelspacing=2)

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_empty = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_empty


def heavy_rain_predinction(predictions):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.now().date()

    # Create an empty array to store the next seven days
    next_seven_days = []

    # Iterate over the range of next seven days and add them to the array
    for i in range(7):
        next_day = current_date + timedelta(days=i+1)
        formatted_date = next_day.strftime("%d/%m/%Y")
        next_seven_days.append(formatted_date)
    #

    pred_no_flood_x = []
    pred_flood_x = []
    pred_no_flood_y = []
    pred_flood_y = []
    for i in range(len(predictions)):
        num = i+1
        if predictions[i][1] <= 0.85:
            pred_no_flood_x.append(num)
            pred_no_flood_y.append(predictions[i][1]*100)
        elif predictions[i][1] > 0.85:
            pred_flood_x.append(num)
            pred_flood_y.append(predictions[i][1]*100)
        #


    threshold = 85

    image_width_px = 1000
    dpi = 100  # Adjust the DPI value as needed
    inches_per_pixel = 1 / dpi
    width_inches = image_width_px * inches_per_pixel
    height_inches = width_inches * 0.6  # Adjust the height ratio as needed


    # Plotting
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 110)

    # Grid lines
    ax.grid(True, linestyle='--', alpha=0.5)

    ax.scatter(pred_no_flood_x, pred_no_flood_y, color='green', s=700, label='No Heavy Rain Event')
    ax.scatter(pred_flood_x, pred_flood_y, color='red', s=700, label='Potential Heavy Rain Event')

    # Threshold line
    ax.plot([0, 8], [threshold, threshold], color='orange', linestyle='--', label='Threshold')

    # Axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Confidence')

    # Ticks
    ax.set_xticks(np.arange(1, 8))
    ax.set_xticklabels(next_seven_days, fontsize=9)
    ax.set_yticks(np.arange(0, 111, 20))

    # Legend
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1) ,borderpad=2,labelspacing=2)

    # Tight layout to prevent label overlap
    plt.tight_layout()

     # Save plot as image file
    # if(city == 'Aachen'):
    #     filename = 'plot_heavy_rain_prediction_aachen.svg'  # Specify the filename and extension
    #     plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_heavy_rain_prediction = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_heavy_rain_prediction


def snow_predinction(predictions):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.now().date()

    # Create an empty array to store the next seven days
    next_seven_days = []

    # Iterate over the range of next seven days and add them to the array
    for i in range(7):
        next_day = current_date + timedelta(days=i+1)
        formatted_date = next_day.strftime("%d/%m/%Y")
        next_seven_days.append(formatted_date)
    #

    pred_no_flood_x = []
    pred_flood_x = []
    pred_no_flood_y = []
    pred_flood_y = []
    for i in range(len(predictions)):
        num = i+1
        if predictions[i][3] <= 0.85:
            pred_no_flood_x.append(num)
            pred_no_flood_y.append(predictions[i][3]*100)
        elif predictions[i][3] > 0.85:
            pred_flood_x.append(num)
            pred_flood_y.append(predictions[i][3]*100)
        #

    threshold = 85

    image_width_px = 1000
    dpi = 100  # Adjust the DPI value as needed
    inches_per_pixel = 1 / dpi
    width_inches = image_width_px * inches_per_pixel
    height_inches = width_inches * 0.6  # Adjust the height ratio as needed

    # Plotting
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 110)

    # Grid lines
    ax.grid(True, linestyle='--', alpha=0.5)

    ax.scatter(pred_no_flood_x, pred_no_flood_y, color='green', s=700, label='No Snow Event')
    ax.scatter(pred_flood_x, pred_flood_y, color='red', s=700, label='Potential Snow Event')

    # Threshold line
    ax.plot([0, 8], [threshold, threshold], color='orange', linestyle='--', label='Threshold')

    # Axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Confidence')

    # Ticks
    ax.set_xticks(np.arange(1, 8))
    ax.set_xticklabels(next_seven_days, fontsize=9)
    ax.set_yticks(np.arange(0, 111, 20))

    # Legend
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1) ,borderpad=2,labelspacing=2)

    # Tight layout to prevent label overlap
    plt.tight_layout()

     # Save plot as image file
    # if(city == 'Aachen'):
    #     filename = 'plot_snow_prediction_aachen.svg'  # Specify the filename and extension
    #     plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_snow_prediction = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_snow_prediction

def others_predinction(predictions_others):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.now().date()

    # Create an empty array to store the next seven days
    next_seven_days = []

    # Iterate over the range of next seven days and add them to the array
    for i in range(7):
        next_day = current_date + timedelta(days=i+1)
        formatted_date = next_day.strftime("%d/%m/%Y")
        next_seven_days.append(formatted_date)
    #

    pred_no_other_x = []
    pred_other_x = []
    pred_no_other_y = []
    pred_other_y = []
    for i in range(len(predictions_others)):
        num = i+1
        if predictions_others[i][2] <= 0.85:
            pred_no_other_x.append(num)
            pred_no_other_y.append(predictions_others[i][2]*100)
        elif predictions_others[i][2] > 0.85:
            pred_other_x.append(num)
            pred_other_y.append(predictions_others[i][2]*100)
        #

    threshold = 85

    image_width_px = 1000
    dpi = 100  # Adjust the DPI value as needed
    inches_per_pixel = 1 / dpi
    width_inches = image_width_px * inches_per_pixel
    height_inches = width_inches * 0.6  # Adjust the height ratio as needed

    # Plotting
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 110)

    # Grid lines
    ax.grid(True, linestyle='--', alpha=0.5)

    ax.scatter(pred_no_other_x, pred_no_other_y, color='green', s=700, label='No Other Events')
    ax.scatter(pred_other_x, pred_other_y, color='red', s=700, label='Potential Other Events')

    # Threshold line
    ax.plot([0, 8], [threshold, threshold], color='orange', linestyle='--', label='Threshold')

    # Axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Confidence')

    # Ticks
    ax.set_xticks(np.arange(1, 8))
    ax.set_xticklabels(next_seven_days, fontsize=9)
    ax.set_yticks(np.arange(0, 111, 20))

    # Legend
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1) ,borderpad=2,labelspacing=2)

    # Tight layout to prevent label overlap
    plt.tight_layout()

     # Save plot as image file
    # if(city == 'Aachen'):
    #     filename = 'plot_other_prediction_aachen.svg'  # Specify the filename and extension
    #     plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_other_prediction = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_other_prediction


# def show_graph_database(type):
#     driver = GraphDatabase.driver("bolt://localhost:7687/neo4j", auth=("neo4j", "password"))
#     with driver.session() as session:
#        # cypher_query = "MATCH (n:Event) RETURN n "
#         cypher_query = "MATCH (a)-[r]->(b) RETURN a, r, b  LIMIT 800"
#         if type == 'Starkregen':
#             cypher_query = "MATCH (a:ScenarioPattern)-[r:hasContext]-> (b:Context) WHERE b.event = 'Starkregen/Hagel' RETURN a,r,b"
#         elif type == 'Hochwasser':
#             cypher_query = "MATCH (a:ScenarioPattern)-[r:hasContext]-> (b:Context) WHERE b.event = 'Hochwasser' RETURN a,r,b"
#
#         result = session.run(cypher_query)
#         graph_data = result.data()
#         # print(graph_data)
#
#     context = {'graph_data': graph_data}
#     # Convert graph_data to JSON string
#     graph_json = json.dumps(context)
#     # print(graph_json)
#
#     return graph_json



# METHODS used for creating the webpage #
def plot_requester_dutyHours():
    # Read CSV into pandas
    price = df_withonout_nan['duty hours']
    name = df_withonout_nan['requester']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Horizontal Bar Plot
    ax.barh(name, price)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Add legend
    ax.legend(['duty hours'])

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_requester_dutyHours.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_requester_dutyHours = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_requester_dutyHours

def plot_requester_helperss():

    # Read CSV into pandas
    price = df_withonout_nan['number of helpers']
    name = df_withonout_nan['requester']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Horizontal Bar Plot
    ax.barh(name, price)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Add legend
    ax.legend(['number of helpers'])

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_requester_helperss.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_requester_helperss = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_requester_helperss

# Table in Data Visual
def get_data():
    # GET DATA
    df = pd.read_excel("missiontask_with_units.xlsx")
    df_withonout_nan = df.dropna()
    df_withonout_nan_custom = df_withonout_nan[['requester','event type', 'mission task', 'description', 'service project', 'number of helpers', 'duty hours', 'ID'] ]
    df_withonout_nan_custom = df_withonout_nan_custom.head(6)
    return df_withonout_nan_custom

def plot_dutyHours_missionTask():

    # Read CSV into pandas
    price = df_withonout_nan['duty hours']
    name = df_withonout_nan['mission task']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 20))

    # Horizontal Bar Plot
    ax.barh(name, price)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Modify the desired tick label (e.g., make it bold and add a note)
    highlight_index = 31  # Index of the tick label you want to highlight
    highlight_label = y_labels[highlight_index]
    highlight_label.set_fontweight('bold')
    highlight_label.set_text(f'{highlight_label.get_text()} (with around 1200 duty hours)')

    # Set the modified tick labels back to the y-axis
    ax.set_yticklabels(y_labels)

    # Add legend
    ax.legend(['duty hours'])

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_dutyHours_missionTask.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_dutyHours_missionTask = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_dutyHours_missionTask

def plot_helpers_missionTask():

    # Read CSV into pandas
    price = df_withonout_nan['number of helpers']
    name = df_withonout_nan['mission task']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 20))

    # Horizontal Bar Plot
    ax.barh(name, price)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Modify the desired tick label (e.g., make it bold and add a note)
    highlight_index = 22  # Index of the tick label you want to highlight
    highlight_label = y_labels[highlight_index]
    highlight_label.set_fontweight('bold')
    highlight_label.set_text(f'{highlight_label.get_text()} (with around 90 helpers)')

    # Set the modified tick labels back to the y-axis
    ax.set_yticklabels(y_labels)

    # Add legend
    ax.legend(['number of helpers'])

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_helpers_missionTask.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_helpers_missionTask = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_helpers_missionTask

def plot_dutyHours_typeOfService():

    # Read CSV into pandas
    hours = df_withonout_nan['duty hours']
    service = df_withonout_nan['type of service']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 4))

    # Horizontal Bar Plot
    ax.barh(service, hours)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Set the modified tick labels back to the y-axis
    ax.set_yticklabels(y_labels)

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_dutyHours_typeOfService.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_dutyHours_typeOfService = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_dutyHours_typeOfService

def plot_helpers_typeOfService():

    # Read CSV into pandas
    helpers = df_withonout_nan['number of helpers']
    service = df_withonout_nan['type of service']

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 4))

    # Horizontal Bar Plot
    ax.barh(service, helpers)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Show top values
    ax.invert_yaxis()

    y_labels = ax.get_yticklabels()  # Get the existing tick labels
    for label in y_labels:
        label.set_fontsize(12)  # Adjust the font size of each label
    x_labels = ax.get_xticklabels()  # Get the existing tick labels
    for label in x_labels:
        label.set_fontsize(12)  # Adjust the font size of each label

    # Set the modified tick labels back to the y-axis
    ax.set_yticklabels(y_labels)

    # Tight layout to prevent label overlap
    plt.tight_layout()

    # Save
    # filename = 'plot_helpers_typeOfService.svg'  # Specify the filename and extension
    # plt.savefig(filename, format='svg')

    # Convert plot to image and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_helpers_typeOfService = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to avoid memory leaks

    return plot_helpers_typeOfService
