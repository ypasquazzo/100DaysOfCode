import requests
import os

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

TOKEN_SHEETY = os.environ.get("TOKEN_SHEETY")
SHEET_ENDPOINT = "0bd443f02447e5aa23864167d6be8f0c"

print("Welcome to Yannick's Flight Club! \nWe find the best flight deals and email you.")

while True:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")
    email_confirmation = input("Type your email again: ")
    if email == email_confirmation:
        break
    else:
        print("Email mismatch. Try again!")

header = {
    "Authorization": "Bearer " + TOKEN_SHEETY,
    "Content-Type": "application/json"
}
parameters = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}
response = requests.post(
    url=f"https://api.sheety.co/{SHEET_ENDPOINT}/100DaysOfCodeFlightDeals/users",
    json=parameters, headers=header)
response.raise_for_status()

print("Searching for good deals...")
data = DataManager()
for deal in data.deals:

    flight_search = FlightSearch(deal)

    if flight_search.data is None:
        continue
    if len(flight_search.data["route"]) == 4:
        flight_data = FlightData(flight_search, stop_overs=1, via_city=flight_search.data["route"][0]["cityTo"])
    else:
        flight_data = FlightData(flight_search)

    if flight_data.price < deal["lowestPrice"]:
        users = DataManager.get_emails()
        notification_manager = NotificationManager(flight_data, users)
        print(f"Found a good deal for {flight_data.to_city}! Sending mails to our users..")
