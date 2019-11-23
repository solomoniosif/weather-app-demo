import weather as w
from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/<city_name>/")
def city_weather(city_name):
    weather_city = w.weather(city_name)
    return render_template('presentweather.html', weather=weather_city)


@app.route("/reqcity/", methods=["GET", "POST"])
def reqcity():
    if request.method == 'POST':
        city = request.form['city']
        weather_city = w.weather_other(city)
        return render_template('presentweather.html', weather=weather_city)
    return render_template('reqcity.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
