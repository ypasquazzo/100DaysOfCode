from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


data = DataManager()
for deal in data.deals:
    flight_search = FlightSearch(deal)
    flight_data = FlightData(flight_search)

    if flight_data.price < deal["lowestPrice"]:
        notification_manager = NotificationManager(flight_data)
