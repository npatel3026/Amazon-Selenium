from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import os

# Get absolute path of geckodriver.exe in the same folder
driver_path = os.path.join(os.getcwd(), "geckodriver.exe")
service = Service(driver_path)

# Create Firefox driver
driver = webdriver.Firefox(service=service)

# Open Amazon
driver.get("https://www.amazon.com")
driver.maximize_window()
time.sleep(2)

# Check title
expected_title = "Amazon.com. Spend less. Smile more."
actual_title = driver.title
if expected_title in actual_title:
    print("Title Test Passed")
else:
    print("Title Test Failed", actual_title)

# Check search bar
try:
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    print("Search Bar Test Passed")
except:
    print("Search Bar Test Failed")

# Check search button
try:
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    print("Search Button Test Passed")
except:
    print("Search Button Test Failed")

# Perform search
search_bar.send_keys("laptop")
search_button.click()
time.sleep(3)

# Check search results
try:
    results = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")
    if len(results) > 0:
        print(f"Search Results Test Passed Total results found: {len(results)}")
    else:
        print("Search Results Test Failed  No results found")
except:
    print("Search Results Test Failed ")

# Close browser
driver.quit()
