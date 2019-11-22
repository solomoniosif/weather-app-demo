import requests
import json
from secret import appid

def weather_cluj():
    city = 'Cluj-Napoca'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_lisbon():
    city = 'Lisbon'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_tirana():
    city = 'Tirana'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_dublin():
    city = 'Dublin'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_budapest():
    city = 'Budapest'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_berlin():
    city = 'Berlin'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_bergen():
    city = 'Bergen'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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


def weather_other():
    try:
        city = input('Enter a city to check the weather')
    except:
        return 'No data could be found for your entry. Try again!'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    response = requests.get(url.format(city, appid))
    r = response.json()

    weather_d = {
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