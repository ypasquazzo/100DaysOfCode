import requests
import os
from twilio.rest import Client

parameters = {

    "lat": 47.6,
    "lon": -2.8,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get('OWM_API_KEY'),

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_data = weather_data["hourly"][:12]
weather_codes = [hour["weather"][0]["id"] for hour in weather_data]
will_rain = any(code < 700 for code in weather_codes)

if will_rain:
    account_sid = 'AC40adb444bd52ee0c7999e4125ee70d42'
    auth_token = os.environ.get("TWILIO_API_KEY")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="It looks like it will rain today, don't forget your umbrella!",
                         from_='+447360540457',
                         to='+447496574267'
                     )

    print(message.status)
