from bs4 import BeautifulSoup
import cloudscraper

from mail import Mail

URL = "https://www.amazon.fr/tablette-fire-hd-10/dp/B08F63PPNV/ref=sr_1_2?crid=Y4R63CR7GC28"
TARGET_PRICE = 150

scraper = cloudscraper.create_scraper()
amazon_page = scraper.get(URL)

soup = BeautifulSoup(amazon_page.text, 'html.parser')

price = float(soup.find(name="span", class_="a-offscreen").text.replace("€", "").replace(",", "."))
title = soup.find(name="span", class_="a-size-large product-title-word-break").text

if price < TARGET_PRICE:
    head = "Low price alert!"
    body = f"{title} is now {price}€.\n {URL}"

    mail = Mail()
    mail.send_message(destination="xxxxxx", subject=head, body=body)
    print("Price is low! Sending an alert...")
