# This code requires the credentials to be stored inside a {creds.json} as follow:
# {
#     "email": "xxxxxx",
#     "password": "xxxxxx",
#     "smtp_server": "xxxxxx"
# }
#

import smtplib
from email.message import EmailMessage
import json

CREDS = "creds.json"


class Mail:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.smtp_server = ""
        self.server = None
        self.configure()
        self.connect()

    def configure(self):
        try:
            with open(file=CREDS, mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File not found. Create a JSON with the credentials.")
        else:
            self.username = data["email"]
            self.password = data["password"]
            self.smtp_server = data["smtp_server"]

    def connect(self):
        self.server = smtplib.SMTP(self.smtp_server, 587)
        self.server.starttls()
        self.server.login(self.username, self.password)

    def send_message(self, destination, subject, body):
        msg = EmailMessage()
        msg.set_content(body)

        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = destination

        self.server.send_message(msg)
        self.server.quit()
