from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, status
from geopy.geocoders import Nominatim

import requests
import numpy as np
from joblib import load
import xgboost as xgb
import pandas as pd


def get_weather_forecast(url):
    res = requests.get(url)
    return res.json()

def get_city_location(city):

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude

def preprocess_response(res):


    # Pressure
    press = (res["hourly"]["pressure_msl"])
    daily_slp = [] 

    num = 7
    try:
        for i in range(7):
            daily_slp.append(np.array(press[24*(i):24*(i+1)]).mean())
    except Exception:
        num = 6

    #  Temprature
    temp = res["hourly"]["temperature_2m"]
    daily_temp = [] 
    for i in range(num):
        daily_temp.append(np.array(temp[24*(i):24*(i+1)]).mean())

    # Dewpoint
    dewp = res["hourly"]["dewpoint_2m"]
    daily_dewp = [] 
    for i in range(num):
        daily_dewp.append(np.array(dewp[24*(i):24*(i+1)]).mean())

    # Windspeed
    wspd = res["hourly"]["windspeed_10m"]
    daily_wspd = [] 
    for i in range(num):
        daily_wspd.append(np.array(wspd[24*(i):24*(i+1)]).mean())

    # Cloudcover
    cldcover = res["hourly"]["cloudcover_low"]
    daily_visibility = [] 
    vals = []
    for i in range(num):
        val = 100 - (np.array(cldcover[24*(i):24*(i+1)]).mean())
        vals.append(val)
        new_value = ( (val - 0) / (100 - 0) ) * (6.20 - 0.6) + 0.6
        daily_visibility.append(new_value)

    print("===========================")
    print(vals)
    print(daily_visibility)

    # Weathercode
    wcode = res["hourly"]["weathercode"]

    # Fog
    daily_fog_indicator = []
    fog_codes = [45, 48]
    for i in range(num):
        daily_fog_indicator.append(any(item in fog_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Drizzle
    drizzle_codes = [51, 53, 55, 56, 57]
    daily_drizzle_indicator = []
    for i in range(num):
        daily_drizzle_indicator.append(any(item in drizzle_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Snow
    snow_codes = [71, 73, 75, 77]
    daily_snow_indicator = []
    for i in range(num):
        daily_snow_indicator.append(any(item in snow_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    # Thunder
    thunder_codes = [95, 96, 99]
    daily_thunder_indicator = []
    for i in range(num):
        daily_thunder_indicator.append(any(item in thunder_codes for item in np.array(wcode[24*(i):24*(i+1)])))

    daily_max_wspd = res["daily"]["windspeed_10m_max"]

    daily_max_wgust = res["daily"]["windgusts_10m_max"]

    daily_max_temp = res["daily"]["temperature_2m_max"]

    daily_min_temp = res["daily"]["temperature_2m_min"]

    daily_prcp = res["daily"]["precipitation_sum"]

    # All days weather
    days_weather = []
    for i in range (num):
        days_weather.append(np.array([daily_temp[i], daily_dewp[i], daily_slp[i], 996.125888, daily_visibility[i], daily_wspd[i], daily_max_wspd[i], daily_max_wgust[i], daily_max_temp[i], daily_min_temp[i], daily_prcp[i], int(daily_fog_indicator[i]), int(daily_drizzle_indicator[i]), int(daily_snow_indicator[i]), int(daily_thunder_indicator[i])]))
    
    if num == 6:
        days_weather.append(days_weather[5])


    original_days_weather = days_weather
    sc=load('scaler.bin')
    days_weather = sc.transform(days_weather)
    return days_weather, original_days_weather


class OutagePredictionViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @action(detail=False, methods=['get'])
    def predict(self, request, *args, **kwargs):

        city = self.request.GET.get('city')

        print("cityy", city)
        # Get city location
        lat, long = get_city_location(city)

        #  Weather API 
        url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=cloudcover_low,weathercode,windspeed_10m,temperature_2m,pressure_msl,dewpoint_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,weathercode,windspeed_10m_max,windgusts_10m_max&temperature_unit=fahrenheit&current_weather=true&windspeed_unit=kn&precipitation_unit=inch&timezone=CET'.format(lat, long)
        res = get_weather_forecast(url)
        data, data_original = preprocess_response(res)

        features_names = ['temp', 'dwep', 'slp', 'stp', 'visibility', 'wspd', 'mxwspd', 'mxwgust', 'mxtemp', 'mintemp', 'prcp', 'fog', 'drizzle', 'snow', 'thunder']
        # Load model
        model = xgb.XGBClassifier()
        model.load_model("model.json")

        # Predict
        preds = model.predict(data)
        prob = model.predict_proba(data)

        confidence = []
        for i in range(len(prob)):
            if preds[i] == 1 and prob[i][1] < 0.85:
                preds[i] = 0
                prob[i][0] = ((prob[i][0] - 0) / (1 - 0)) * (1 - 0.5) + 0.5
                confidence.append(prob[i][0])
                continue
            elif preds[i] == 1 and prob[i][1] >= 0.85:
                new_value = ((prob[i][1] - 0.50) / (1 - 0.5) ) * (0.9 - 0.3) + 0.3
                confidence.append(new_value)
                continue
            else:
                new_value = ((prob[i][preds[i]] - 0.50) / (1 - 0.5) ) * (0.96 - 0.5) + 0.5
                confidence.append(new_value)
        print("preds ", preds)
        print("--------------")
        print("confidence ", confidence)
        print("--------------")
        print("data_original", data_original)
        print("--------------")
        print("Features", features_names)
	
	
        return Response({'Predictions': preds,
                         'Confidence': np.around(np.array(confidence), decimals=4),
                         'Features': features_names,
                         'Weather': np.around(np.array(data_original), decimals=2),
        }, status=status.HTTP_200_OK)

