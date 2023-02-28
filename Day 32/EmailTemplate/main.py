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

username = ""
password = ""
smtp_server = ""

try:
    with open(file="creds.json", mode="r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found. Create a JSON with the credentials.")
else:
    username = data["email"]
    password = data["password"]
    smtp_server = data["smtp_server"]

# connect to the Hotmail SMTP server
server = smtplib.SMTP(smtp_server, 587)
server.starttls()

# login to the Hotmail SMTP server
server.login(username, password)

# create the message
msg = EmailMessage()
msg.set_content("This is the email body.")

msg['Subject'] = "Test email"
msg['From'] = "xxxxxx"
msg['To'] = "xxxxxx"

# send the email
server.send_message(msg)

# disconnect from the Hotmail SMTP server
server.quit()
