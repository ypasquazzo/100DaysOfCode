import requests
import datetime as dt
import os

SHEET_ENDPOINT = "0bd443f02447e5aa23864167d6be8f0c"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
DEPART_CITY = "LON"


class FlightSearch:

    def __init__(self, deal: dict):
        self.city = deal["iataCode"]
        self.price = deal["lowestPrice"]
        self.data = self.search_flight()

    def search_flight(self):

        headers = {
            "accept": "application/json",
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": DEPART_CITY,
            "fly_to": self.city,
            "date_from": dt.date.today().strftime('%d/%m/%Y'),
            "return_from": dt.date.today().strftime('%d/%m/%Y'),
            "date_to": (dt.date.today() + dt.timedelta(days=6*30)).strftime('%d/%m/%Y'),
            "return_to": (dt.date.today() + dt.timedelta(days=6 * 30)).strftime('%d/%m/%Y'),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 20,
            "flight_type": "round",
            "max_stopovers": 0
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search?", params=params, headers=headers)
        response.raise_for_status()

        info = None
        try:
            info = response.json()["data"][0]
        except IndexError:
            params = {
                "fly_from": DEPART_CITY,
                "fly_to": self.city,
                "date_from": dt.date.today().strftime('%d/%m/%Y'),
                "return_from": dt.date.today().strftime('%d/%m/%Y'),
                "date_to": (dt.date.today() + dt.timedelta(days=6 * 30)).strftime('%d/%m/%Y'),
                "return_to": (dt.date.today() + dt.timedelta(days=6 * 30)).strftime('%d/%m/%Y'),
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 20,
                "flight_type": "round",
                "max_sector_stopovers": 1,
                "limit": 3
            }
            response = requests.get(url="https://api.tequila.kiwi.com/v2/search?", params=params, headers=headers)
            response.raise_for_status()
            info = response.json()["data"][0]
        finally:
            return info

    @staticmethod
    def get_iata_city_code(destinations: list):

        codes = []
        headers = {
            "accept": "application/json",
            "apikey": TEQUILA_API_KEY
        }
        for city in destinations:
            params = {
                "term": city,
                "location_types": "city",
                "limit": 1
            }
            response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            codes.append(data["locations"][0]["code"])

        return codes
