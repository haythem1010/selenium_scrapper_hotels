from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

brave_path = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = r"C:/Users/hayth/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"


options = webdriver.ChromeOptions()
options.binary_location = brave_path

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

# website = get_my_website('booking')
driver.get(f'https://community.brave.com/t/why-brave-selenium-is-different-with-no-selenium/587584')


print(driver.title)

time.sleep(60*60)
driver.close()
