import requests
import datetime as dt
import os

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
TOKEN_SHEETY = os.environ.get("TOKEN_SHEETY")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}
workout = input("What did you do today? ")
parameters = {
    "query": workout,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 32
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

header = {"Authorization": "Bearer " + TOKEN_SHEETY}

date = dt.date.today().strftime('%d/%m/%Y')
current_hour = dt.datetime.now().strftime("%H:00:00")

for activity in data["exercises"]:
    exercise = activity["name"]
    duration = activity["duration_min"]
    calories = activity["nf_calories"]

    workout = {
        "workout": {
            "date": date,
            "time": current_hour,
            "exercise": exercise,
            "duration": str(round(duration))+"min",
            "calories": round(calories)
        }
    }

    response = requests.post(url=f"https://api.sheety.co/{SHEET_ENDPOINT}"
                                 "/100DaysOfCodeMyWorkouts/workouts", json=workout, headers=header)
