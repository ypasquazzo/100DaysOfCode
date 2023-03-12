from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:/Users/Yannick/Documents/Coding Projects/Python/chromedriver.exe"


class AddressScraper:
    def __init__(self, nb_listings: int):
        self.listing = {}
        self.nb = nb_listings
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_listings(self):
        self.driver.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%"
                        "7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.86722876453969%2C%22east%22%3A-122.26904956225586%"
                        "2C%22south%22%3A37.68324067336847%2C%22west%22%3A-122.59760943774414%7D%2C%22isMapVisible%22%"
                        "3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22"
                        "min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C"
                        "%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B"
                        "%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%"
                        "3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22"
                        "regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%"
                        "22%3A12%7D")

        time.sleep(3)

        listing = []
        i = 1
        count = 0
        while True:
            try:
                if i == 3 or i == 17:
                    pass
                else:
                    address = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/'
                                                                 f'li[{i}]/div/div/article/div/div[1]/a/address')

                    price = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/'
                                                               f'li[{i}]/div/div/article/div/div[1]/div[2]/span')

                    url = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul/'
                                                             f'li[{i}]/div/div/article/div/div[1]/a')

                    listing.append({
                        "address": address.get_attribute('innerHTML'),
                        "price": price.get_attribute('innerHTML').split("/")[0].split(" ")[0].split("+")[0],
                        "url": url.get_attribute('href')})
                    count += 1

                if count == self.nb:
                    break

            except NoSuchElementException:
                i = 0
                self.driver.find_element(By.XPATH, '//*[@id="grid-search-results"]/div[2]/nav/ul/li[10]/a').click()
                time.sleep(3)

            i += 1

        self.listing = listing
        self.driver.close()
