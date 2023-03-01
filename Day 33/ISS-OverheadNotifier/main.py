import requests
import datetime as dt
from mail import Mail

MY_LAT = 51.5
MY_LONG = 0.0
MY_EMAIL = "xxxxxx"

parameters = {

    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response_time = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_time.raise_for_status()

data_time = response_time.json()
sunrise = data_time["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_time["results"]["sunset"].split("T")[1].split(":")[0]
time_now = dt.datetime.now().hour

if sunset <= time_now or sunrise >= time_now:
    response_location = requests.get("http://api.open-notify.org/iss-now.json")
    response_location.raise_for_status()

    data_location = response_location.json()
    latitude = data_location["lat"]
    longitude = data_location["lng"]

    if abs(latitude-MY_LAT) < 3 and abs(longitude-MY_LONG) < 3:
        mail = Mail()
        mail.send_message(MY_EMAIL, "Look up!", "The ISS is currently passing over your head.")
