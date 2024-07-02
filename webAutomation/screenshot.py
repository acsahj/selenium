from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


print("Current Working Directory: ", os.getcwd())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, ".btn_action").click()


screenshot_path = os.path.join(os.getcwd(), 'logged_in_homepage.png')

try:
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")
except Exception as e:
    print(f"Error saving screenshot: {e}")

driver.quit()

#Script to login , validate login , add an item in the cart and validate the item in the cart and take screenshots for every navigation