from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding Projects/Python/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

# 1. Get hold of the total number of Wiki pages:
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# pages_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(pages_count.get_attribute("innerHTML"))

# 2. Click on the link for the total number of pages:
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# pages_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# pages_count.click()

# 3. Type test into the search input:
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# 4. Fill out a form and log into a website:
driver.get("https://web.archive.org/web/20190201181142/http://secure-retreat-92358.herokuapp.com:80/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Name")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Surname")
email = driver.find_element(By.NAME, "email")
email.send_keys("test@mail.com")
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()

driver.quit()
