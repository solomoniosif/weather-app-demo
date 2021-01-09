import requests
import json
from secret import appid

def weather(city_name):
    city = city_name
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
        'long': r['coord']['lon'],
        'lati': r['coord']['lat'],
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'pressure': r['main']['pressure'],
        'humidity': r['main']['humidity'],
        'temp_min': r['main']['temp_min'],
        'temp_max': r['main']['temp_max'],
        'wind_speed': r['wind']['speed']
    }
    return weather_d

def weather_other(city):
    weather_d = weather(city)
    return weather_d
