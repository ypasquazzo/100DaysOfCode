from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding Projects/Python/chromedriver.exe"
TWITTER_USERNAME = "xxxxxx"
TWITTER_HANDLE = "xxxxxx"
TWITTER_PASSWORD = "xxxxxx"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(CHROME_DRIVER_PATH)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                           '/div[3]/div[1]/a/span[4]').click()
        time.sleep(45)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                           '/div/div[8]/div/div/div[2]/a').click()
        time.sleep(1)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                           '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]'
                                                           '/span').get_attribute("innerHTML"))
        time.sleep(1)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                             '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                             'div[2]/span').get_attribute("innerHTML"))

    def tweet_speed(self):
        tweet = f"100 Days of Code #51 - Internet speed is {self.down}Mb/s up and {self.up}Mb/s up."

        self.driver.get("https://twitter.com/i/flow/login")
        self.driver.maximize_window()

        time.sleep(1)
        un = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                'div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        un.send_keys(TWITTER_USERNAME)
        un.send_keys(Keys.ENTER)
        time.sleep(1)
        check = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                   '/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        # Comment the next part if no confirmation requested.
        check.send_keys(TWITTER_HANDLE)
        check.send_keys(Keys.ENTER)
        time.sleep(1)
        pw = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]'
                                                '/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw.send_keys(TWITTER_PASSWORD)
        pw.send_keys(Keys.ENTER)
        time.sleep(20)  # Gives time to enter mail confirmation code if requested
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]'
                                           '/div[3]/a/div').click()
        time.sleep(1)
        tweet_input = self.driver.switch_to.active_element
        tweet_input.send_keys(tweet)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/'
                                           'div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
                                           '/div/span').click()
