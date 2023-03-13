from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    current_year = dt.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<name>')
def check_name(name):

    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    gender = response.json()["gender"]
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    age = response.json()["age"]

    current_year = dt.datetime.now().year
    return render_template("index.html", year=current_year, name=name.capitalize(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
