import requests
import os
import json

from flight_search import FlightSearch

TOKEN_SHEETY = os.environ.get("TOKEN_SHEETY")
SHEET_ENDPOINT = "0bd443f02447e5aa23864167d6be8f0c"
TEQUILA_API_KEY = "rzKd700d2btT1bRCliS6v0Nyio-6Z4Tb"


class DataManager:

    def __init__(self):

        # This only needs to be run once:
        # self.initialize_iata_codes()
        self.deals = self.get_data()

    @staticmethod
    def get_data():
        # header = {"Authorization": "Bearer " + TOKEN_SHEETY}
        # response = requests.get(url=f"https://api.sheety.co/{SHEET_ENDPOINT}/"
        #                             f"100DaysOfCodeFlightDeals/prices", headers=header)
        # response.raise_for_status()
        # data = response.json()

        # data copied in Json to not call the Sheety API every time (limited access)
        with open('data.json', 'r') as f:
            data = json.load(f)

        return data["prices"]

    @staticmethod
    def get_emails():
        header = {"Authorization": "Bearer " + TOKEN_SHEETY}
        response = requests.get(url=f"https://api.sheety.co/{SHEET_ENDPOINT}/"
                                    f"100DaysOfCodeFlightDeals/users", headers=header)
        response.raise_for_status()
        data = response.json()

        return [user["email"] for user in data["users"]]

    @staticmethod
    def get_cities():
        header = {"Authorization": "Bearer " + TOKEN_SHEETY}
        response = requests.get(url=f"https://api.sheety.co/{SHEET_ENDPOINT}/"
                                    f"100DaysOfCodeFlightDeals/prices", headers=header)
        response.raise_for_status()
        data = response.json()

        return [item['city'] for item in data['prices']]

    @staticmethod
    def put_iata_code(city_codes: dict):
        header = {"Authorization": "Bearer " + TOKEN_SHEETY}
        line = 2

        for city, code in city_codes.items():
            parameters = {
                "price": {
                    "city": city,
                    "iataCode": code
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/{SHEET_ENDPOINT}/100DaysOfCodeFlightDeals/prices/{line}",
                json=parameters, headers=header)
            response.raise_for_status()
            line += 1

    @staticmethod
    def initialize_iata_codes():
        destinations = DataManager.get_cities()
        codes = FlightSearch.get_iata_city_code(destinations)
        city_codes = {destinations[i]: codes[i] for i in range(len(destinations))}
        DataManager.put_iata_code(city_codes)
