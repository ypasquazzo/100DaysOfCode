from flight_search import FlightSearch


class FlightData:

    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search
        self.from_city = self.flight_search.data["cityFrom"]
        self.to_city = self.flight_search.data["cityTo"]
        self.from_airport = self.flight_search.data["flyFrom"]
        self.to_airport = self.flight_search.data["flyTo"]
        self.price = self.flight_search.data["price"]
        self.date_from = self.flight_search.data["route"][0]["local_departure"].split("T")[0]
        self.date_to = self.flight_search.data["route"][1]["local_arrival"].split("T")[0]
