from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Launch the page
driver.get("https://www.saucedemo.com/")
# Maximize the browser window
driver.maximize_window()
# Test data
username = "standard_user"
password = "secret_sauce"
# Locate the username field and enter the username
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(username)
# Locate the password field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
# Locate the login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
# Verify the login by checking the presence of an element on the homepage
# (e.g., a product title or any other element unique to the homepage)
try:
    homepage_element = driver.find_element(By.CLASS_NAME, "title")
    print("Login successful!")
except:
    print("Login failed!")
# Close the browser
#driver.quit()

