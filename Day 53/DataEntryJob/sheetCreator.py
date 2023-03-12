import requests
import os

TOKEN_SHEETY = os.environ.get("TOKEN_SHEETY")
SHEET_ENDPOINT = "0bd443f02447e5aa23864167d6be8f0c"


class SheetCreator:
    def __init__(self, listings: list):
        self.listings = listings

    def add_listings_to_sheet(self):
        header = {
            "Authorization": f"Bearer viabuwfbauugbibarvni",
            "Content-Type": "application/json"
        }

        for i in range(0, len(self.listings)):
            parameters = {
                "listing": self.listings[i]
            }
            response = requests.post(url=f"https://api.sheety.co/0bd443f02447e5aa23864167d6be8f0c/"
                                         f"100DaysOfCodeRentalListings/listings",
                                     headers=header, json=parameters)
            response.raise_for_status()
