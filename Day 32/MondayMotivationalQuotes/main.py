import smtplib
from email.message import EmailMessage
import json
import random
import datetime as dt

username = ""
password = ""
smtp_server = ""
quotes_list = []

if dt.datetime.now().weekday() == 1:

    with open(file="quotes.txt", mode="r") as f:
        quotes_list = f.readlines()
    quote = random.choice(quotes_list).replace(" - ", "\n")

    try:
        with open(file="creds.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found. Create a JSON with your credentials.")
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
    msg.set_content(quote)

    msg['Subject'] = "Quote of the day"
    msg['From'] = "xxxxxx"
    msg['To'] = "xxxxxx"

    # send the email
    server.send_message(msg)

    # disconnect from the Hotmail SMTP server
    server.quit()
