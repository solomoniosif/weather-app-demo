import weather as w
from flask import Flask, render_template, request
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '8e532a95c1956ca19d07c3a4cc6f0fe9'

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/cluj/")
def cluj():
    weather_cluj = w.weather_cluj()
    return render_template('presentweather.html', weather=weather_cluj)


@app.route("/lisbon/")
def lisbon():
    weather_lisbon = w.weather_lisbon()
    return render_template('presentweather.html', weather=weather_lisbon)

@app.route("/tirana/")
def tirana():
    weather_tirana = w.weather_tirana()
    return render_template('presentweather.html', weather=weather_tirana)

@app.route("/dublin/")
def dublin():
    weather_dublin = w.weather_dublin()
    return render_template('presentweather.html', weather=weather_dublin)


@app.route("/budapest/")
def budapest():
    weather_budapest = w.weather_budapest()
    return render_template('presentweather.html', weather=weather_budapest)

@app.route("/berlin/")
def berlin():
    weather_berlin = w.weather_berlin()
    return render_template('presentweather.html', weather=weather_berlin)


@app.route("/bergen/")
def bergen():
    weather_bergen = w.weather_bergen()
    return render_template('presentweather.html', weather=weather_bergen)


@app.route("/reqcity/", methods=["GET", "POST"])
def reqcity():
    if request.method == 'POST':
        city = request.form['city']
        weather_city = w.weather_other(city)
        return render_template('presentweather.html', weather=weather_city)
    return render_template('reqcity.html')
    


if __name__ == "__main__":
    app.run(debug=True, port=5000)
