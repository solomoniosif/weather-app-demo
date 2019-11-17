import json

from flask import Flask

import weather

app = Flask(__name__)

@app.route("/")
def hello():
    return "Salut! \nDe unde ne comandam de mancare azi?"

@app.route("/weather/")
def weathe_route():
    temp = json.dumps(weather.weather())
    return temp


@app.route("/weather/my-cities")
def weather_multiple_cities():
    return "Cluj: 15, New York: 10"