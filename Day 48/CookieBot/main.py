from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding Projects/Python/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(By.CLASS_NAME, "grayed")
item_ids = [item.get_attribute("id") for item in items]
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60*5
time_to_buy = time.time() + 5
while True:
    cookie.click()

    if time.time() > time_to_buy:
        money = int(driver.find_element(By.ID, "money").get_attribute("innerHTML").replace(",", ""))

        prices = []
        for item in item_ids:
            price = driver.find_element(By.XPATH, f'//*[@id="{item}"]/b')
            prices.append(int(price.get_attribute('innerHTML').split(" ")[-1].replace(",", "")))

        buying_price = [p for p in prices if p <= money]
        item_to_buy = driver.find_element(By.ID, item_ids[prices.index(max(buying_price))])
        item_to_buy.click()

        time_to_buy = time.time() + 5

    if time.time() > timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        break

driver.quit()
