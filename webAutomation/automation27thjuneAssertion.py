#Validating the login process
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Firefox()
username = "standard_user"
password = "secret_sauce"
driver.get("https://www.saucedemo.com/")
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(username)
# Locate the password field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
#assertion for input values which is login and password
assert "inventory" in driver.current_url
print("Login Successful")