import os
from twilio.rest import Client

from flight_data import FlightData


class NotificationManager:

    def __init__(self, flight_data: FlightData):
        self.data = flight_data
        self.send_alert()

    def send_alert(self):
        account_sid = 'AC40adb444bd52ee0c7999e4125ee70d42'
        auth_token = os.environ.get("TWILIO_API_KEY")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=f"Low price alert! Only €{self.data.price} to fly from {self.data.from_city}-"
                     f"{self.data.from_airport} to {self.data.to_city}-{self.data.to_airport}, "
                     f"from {self.data.date_from} to {self.data.date_to}",
                from_=os.environ.get("TWILIO_NUMBER"),
                to='+44123456789'
            )

        print(message.status)
