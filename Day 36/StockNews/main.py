import os
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then implement STEP 2.
alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": os.environ.get("ALPHA_API_KEY")
}

response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
response.raise_for_status()
data_stock = response.json()

today = dt.date.today()
two_days_ago = today - dt.timedelta(days=2)
yesterday = today - dt.timedelta(days=1)

price_two_days_ago = float(data_stock["Time Series (Daily)"][str(two_days_ago)]['1. open'])
price_yesterday = float(data_stock["Time Series (Daily)"][str(yesterday)]['4. close'])

if abs(price_two_days_ago - price_yesterday) > price_two_days_ago * 0.05:
    # # STEP 2: Use https://newsapi.org
    # Get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "from": str(two_days_ago),
        "sortBy": "popularity",
        "pageSize": 3,
        "apikey": os.environ.get("NEWS_API_KEY"),
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    data_news = response.json()['articles']

    news_list = [{"journal": news["author"],
                  "title": news["title"],
                  "description": news["description"]}
                 for news in data_news]

    # # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    account_sid = 'AC40adb444bd52ee0c7999e4125ee70d42'
    auth_token = os.environ.get("TWILIO_API_KEY")
    client = Client(account_sid, auth_token)

    price_diff = price_two_days_ago - price_yesterday
    if price_diff < 0:
        body = f"TSLA: 🔻{round(price_diff)}%\n"
    else:
        body = f"TSLA: 🔺{round(price_diff)}%\n"

    for news in news_list:
        body += f"Journal: {news['journal']}\n" + f"Headline: {news['title']}\n" + f"Brief: {news['description']}\n"

    message = client.messages.create(
                body=body,
                from_='+44123456789',
                to='+44987654321')
