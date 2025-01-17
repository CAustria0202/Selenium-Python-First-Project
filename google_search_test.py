#Test using Elements on Selenium
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to Google
driver.get("https://google.com")

# Locate the Google search box
googleSearchBox = driver.find_element(By.ID, "APjFqb")
googleSearchBox.send_keys("Automation")

#OPTION 2;
# Wait for the search button to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK"))).click()

# Wait for 5 seconds to observe the result (optional)
time.sleep(5)

#Quit the Driver
driver.quit()