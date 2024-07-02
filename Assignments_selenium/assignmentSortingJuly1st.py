import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
import re
import time
class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

#Test Case 1: Successful Login
    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.assertIn("Swag Labs", self.driver.title)
        screenshot_path = os.path.join(os.getcwd(), 'logged_in_homepage.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

#Test Case 2: Unsuccessful Login with Incorrect Password
    def test_incorrect_password_login(self):
        #Navigate to the SauceDemo login page.
        self.driver.get("https://www.saucedemo.com/")
        #Enter correct username and wrong password.
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("test")
        #Click the login button
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        #Validate the error message
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        error_message=self.driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text
        self.assertEqual(expected_error,error_message,"Login error message doesn't match")
        print("Displayed error message is correct")
        screenshot_path = os.path.join(os.getcwd(), 'incorrect_password_login.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")


#Test Case 3: Verify product sorting by price.
    def test_sort_low_to_high(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.driver.find_element(By.CLASS_NAME,"product_sort_container").click()
        self.driver.find_element(By.XPATH, '//option[text()="Price (high to low)"]').click()
        time.sleep(5)
        products= self.driver.find_elements(By.CLASS_NAME,"inventory_list")
        prices= []
        for i in products:
            price=i.find_element(By.CLASS_NAME,"inventory_item_price").text
            price_value = float(re.sub(r'[^\d.]', '', price))
            prices.append(price_value)
        sorted_price=sorted(prices)
        self.assertEqual(prices,sorted_price,"Prices are not sorted from high to low")

        screenshot_path = os.path.join(os.getcwd(), 'sort_high_to_low.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

#Test Case 4: Add Item to Cart
    def test_add_to_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        item_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_description = self.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        cart_item_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        cart_item_description = self.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text
        self.assertEqual(item_description, cart_item_description, f"Text mismatch, main page: {item_description}, cart: {cart_item_description}")
        print("Validation passed: texts are same")
        screenshot_path = os.path.join(os.getcwd(), 'add_to_cart.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")
    
    #Test Case 5: Remove Item from Cart
    def test_remove_from_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
        self.driver.find_element(By.ID,"continue-shopping").click()
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").is_displayed()
        screenshot_path = os.path.join(os.getcwd(), 'remove_from_cart.png')
        screenshot_path = os.path.join(os.getcwd(), 'remove_from_cart.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSauceDemo('test_sort_low_to_high'))
    runner = HtmlTestRunner.HTMLTestRunner(output='reports')
    runner.run(suite)           