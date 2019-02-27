import requests
import os
from datetime import datetime

def main():
    #These get the key and then make a parameter query
    key = os.environ.get('WEATHER_KEY')
    query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

    #creates and calls the url + the parameter query from above
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    
    #makes list for weather
    forecast_items = data['list']

    #finds and prints the proper material
    for forecast in forecast_items:
        #I will us local time to so the user can follow it in their time.
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        weather_description = forecast['weather']['description']
        wind_speed = forecast['wind']['speed']
        print(f'At {date} the temp is {temp}, the weather is {weather_description}, and the wind speed is {wind_speed}')
        

if __name__ == '__main__':
    main()