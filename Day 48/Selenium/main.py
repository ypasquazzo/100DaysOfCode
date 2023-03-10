from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding Projects/Python/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

# 1. Get price from Amazon page:
# driver.get("https://www.amazon.fr/tablette-fire-hd-10/dp/B08F63PPNV/ref=sr_1_2?crid=Y4R63CR7GC28")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute('innerHTML'))

# 2. Get upcoming events from Python.org page:
driver.get("https://www.python.org/")

events = {}
i = 1
while True:
    try:
        date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
        name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
        events.update({i - 1: {"time": date.get_attribute('innerHTML').replace("</span>", "").split(">")[1],
                               "name": name.get_attribute('innerHTML')}
                       })
        i += 1
    except NoSuchElementException:
        break

print(events)
driver.quit()
