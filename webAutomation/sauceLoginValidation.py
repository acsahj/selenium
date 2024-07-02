from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import sauceDemoLogin
import unittest
import HtmlTestRunner

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Launch the page
driver.get("https://www.saucedemo.com/")
test="Epic sadface: Username and password do not match any user in this service"


# Maximize the browser window
driver.maximize_window()



# Locate the username field and enter the username
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(sauceDemoLogin.username)



# Locate the password field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(sauceDemoLogin.password)



# Locate the login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
loginError=driver.find_element(By.CLASS_NAME,"error-button").text
assert test==loginError, "Login failed"
print("Login successful")


#Locate the current working directory
print("Current Working Directory: ", os.getcwd())
screenshot_path = os.path.join(os.getcwd(), 'logged_in_homepage.png')
driver.save_screenshot(screenshot_path)


#Add item to cart and validate the item name and description
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
element_by_class=driver.find_element(By.CLASS_NAME, "inventory_item_name ")
texted=element_by_class.text
description=driver.find_element(By.CLASS_NAME,"inventory_item_desc").text
print(description)
print(texted)
driver.find_element(By.ID,"shopping_cart_container").click()
backpack=driver.find_element(By.CLASS_NAME,"inventory_item_name")
cartPage_Description=driver.find_element(By.CLASS_NAME,"inventory_item_desc").text
texteds=backpack.text
print(texteds)
print(cartPage_Description)
assert description==cartPage_Description,f"Text mismatch,main page:{description},cart:{cartPage_Description}"
print("Validation passed:texts are same")


class TestSauceDemo(unittest.TestCase):
    def test_login(self):
        self.driver.get("https://www.saucedemo.com/") 
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user") 
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce") 
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click() 
        # Assert title self.assertIn("Swag Labs", self.driver.title) 
        # # Take screenshot
        screenshot_path = os.path.join(os.getcwd(), 'logged_in_homepage.png') 
        try: 
           self.driver.save_screenshot(screenshot_path)
           print(f"Screenshot saved at {screenshot_path}")  
        except Exception as e: 
            print(f"Error saving screenshot: {e}")
        
if __name__ == "__main__": unittest.main()
            
        









