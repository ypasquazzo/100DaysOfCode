import pandas
import datetime as dt
from random import randint
import smtplib
from email.message import EmailMessage
import json

NB_LETTERS = 3
letters = []


def sen_email(address, body):
    username = ""
    password = ""
    smtp_server = ""

    try:
        with open(file="creds.json", mode="r") as file:
            creds = json.load(file)
    except FileNotFoundError:
        print("File not found. Create a JSON with the credentials.")
    else:
        username = creds["email"]
        password = creds["password"]
        smtp_server = creds["smtp_server"]

    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(username, password)

    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = "Happy birthday!"
    msg['From'] = username
    msg['To'] = address

    server.send_message(msg)
    server.quit()


for i in range(0, NB_LETTERS):
    with open(file="letter_templates/letter_" + str(i + 1) + ".txt", mode="r") as f:
        letters.append(f.read())

data = pandas.read_csv("birthdays.csv")
birthdays = [row['name'] for index, row in data.iterrows()
             if row['month'] == dt.datetime.now().month and row['day'] == dt.datetime.now().day]

for birthday in birthdays:
    letter = letters[randint(0, NB_LETTERS-1)].replace("[NAME]", birthday)
    mail = data[data.name == birthday]["email"].values[0]
    sen_email(mail, letter)
