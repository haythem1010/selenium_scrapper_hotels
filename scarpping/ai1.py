# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
#
# options = webdriver.ChromeOptions()
# options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
#
# # Essential options
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--user-data-dir=C:/Temp/BraveProfile")
#
# # Disable Brave-specific features that might interfere
# options.add_argument('--disable-brave-extension')
# options.add_argument('--disable-brave-update')
#
# try:
#     service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.get("https://www.google.com")
#     print("Page title:", driver.title)
#     input("Press Enter to close...")  # Keeps browser open for inspection
#     driver.quit()
# except Exception as e:
#     print("Error:", e)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# Configure Brave options
chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Verify this path

# Essential arguments
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--user-data-dir=C:/Temp/BraveProfile")  # Create this folder first

# Disable Brave shields and updates
chrome_options.add_argument('--disable-brave-extension')
chrome_options.add_argument('--disable-brave-update')

try:
    # Setup WebDriver
    service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Test connection
    driver.get("https://www.google.com")
    print("Success! Page title:", driver.title)

    # Keep browser open for inspection
    input("Press Enter to quit...")
    driver.quit()

except Exception as e:
    print(f"Failed to initialize WebDriver: {str(e)}")
    if 'driver' in locals() and driver is not None:
        driver.quit()