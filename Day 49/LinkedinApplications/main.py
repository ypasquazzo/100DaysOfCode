from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding/Python/chromedriver.exe"
USERNAME = "xxxxxx"
PASSWORD = "xxxxxx"
JOB_URL = "YOUR_JOB_URL"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
button = driver.find_element(By.CLASS_NAME, "login__form_action_container")
button.click()

time.sleep(2)
driver.get(JOB_URL)
time.sleep(2)

button_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
button_apply.click()
prefix = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-'
                                       'applyformcommon-easyApplyFormElement-3502860782-83379203-phoneNumber-country"]')
prefix.click()
prefix.send_keys("United Kingdom")
prefix.send_keys(Keys.ENTER)
phone_number = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
                                             '-applyformcommon-easyApplyFormElement-3502860782-83379203-'
                                             'phoneNumber-nationalNumber"]')
phone_number.send_keys("xxxxxx")
button_next = driver.find_element(By.XPATH, '//*[@id="ember245"]')
button_next.click()
button_review = driver.find_element(By.XPATH, '//*[@id="ember249"]')
button_review.click()
button_submit = driver.find_element(By.XPATH, '//*[@id="ember259"]')
button_submit.click()

# Skipping the part where you have to multi-apply, basically same kind of procedure.
