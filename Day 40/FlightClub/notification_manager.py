from flight_data import FlightData
from mail import Mail


class NotificationManager:

    def __init__(self, flight_data: FlightData, users: list):
        self.data = flight_data
        self.users = users
        self.send_alert()

    def send_alert(self):

        if self.data.stop_overs == 0:
            msg = f"Only €{self.data.price} to fly from {self.data.from_city}-" \
                  f"{self.data.from_airport} to {self.data.to_city}-{self.data.to_airport}, " \
                  f"from {self.data.date_from} to {self.data.date_to}."
        else:
            msg = f"Only €{self.data.price} to fly from {self.data.from_city}-" \
                  f"{self.data.from_airport} to {self.data.to_city}-{self.data.to_airport}, " \
                  f"from {self.data.date_from} to {self.data.date_to}.\n" \
                  f"Flight has 1 stop over, via {self.data.via_city}."

        for user in self.users:
            mail = Mail()
            mail.configure()
            mail.connect()
            mail.send_message(destination=user, subject="Low price alert!", body=msg)
