#Scrolling the window
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
time.sleep(2)

#Scrolling to a particular element of the page
# element = driver.find_element(By.ID, "item_3_title_link")
# driver.execute_script("arguments[0].scrollIntoView();", element)
# print(element.text)

# #Scrolling to the bottom of the page.
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# #Scrolling based on pixel
# driver.execute.script("window.scrollBy(0,500)")

#Exercise:Write a script to scroll to the bottom of the inventory page on SauceDemo and print the title of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
print(driver.title)

#Standard Xpath format: 
#By.XPATH, f"//div[text()='{product_name}']"
#Exercise: Write a script to scroll to a specific product on the inventory page and print the product name
#element=driver.find_element(By.XPATH,f"//div[text()='{inventory_item_name}']")
#driver.execute_script("window.scrollTo(arguments[0].scrollIntoView();",element)
