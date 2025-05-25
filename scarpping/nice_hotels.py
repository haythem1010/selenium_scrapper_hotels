from pprint import pprint
from xml.etree.ElementTree import indent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

"""
    hotels Xpath : //div [@id="listing"]//div[@id="search-results"]//div[@class="hotel-name"]
"""

brave_path = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = r"C:/Users/hayth/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"


options = webdriver.ChromeOptions()
options.binary_location = brave_path

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(f'https://hotelnice.fr/recherche?search%5Bcheckin%5D=2025-05-27&search%5Bcheckout%5D=2025-05-29&search%5Badults%5D=2&hidden-booking-iata=NCE#search-results')
time.sleep(3)
hotels = []
hotels_driver = driver.find_elements(By.XPATH, "//div[@id='listing']//div[@id='search-results']//div[@class='hotel-header']")

for hotel in hotels_driver:
    name = hotel.find_element(By.CLASS_NAME, "hotel-name").text
    stars = len(hotel.find_elements(By.XPATH, ".//div[@class='rating']//i[contains(@class, 'voted')]"))
    try:
        score = hotel.find_element(By.CLASS_NAME, "score-note").text
    except NoSuchElementException:
        score = "0"
    try:
        review = hotel.find_element(By.CLASS_NAME, "score-label").text
    except NoSuchElementException:
        review = "0"
    hotels.append({'hotel': name, 'stars': stars, 'score': score, 'review': review})

output_file = "hotels_data.json"


with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(hotels, f, ensure_ascii=False, indent=4)
print(f"Successfully saved {len(hotels)} hotels to {output_file}")

time.sleep(2)
driver.close()
