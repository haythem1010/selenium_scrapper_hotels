from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

brave_path = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = r"C:/Users/hayth/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"


options = webdriver.ChromeOptions()
options.binary_location = brave_path

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# website = get_my_website('booking')
driver.get(f'https://hotelnice.fr/recherche?search%5Bcheckin%5D=2025-05-27&search%5Bcheckout%5D=2025-05-29&search%5Badults%5D=2&hidden-booking-iata=NCE#search-results')
time.sleep(3)
# hotels Xpath : //div [@id="listing"]//div[@id="search-results"]//div[@class="hotel-name"]
hotels = []
hotels_driver = driver.find_elements(By.XPATH, "//div[@id='listing']//div[@id='search-results']//div[@class='hotel-header']")
for hotel in hotels_driver:
    hotels.append(hotel.text)

pprint(hotels)

time.sleep(60*60)
driver.close()
