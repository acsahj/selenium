#Sorting on Saucelabs(Abhishek's solution to the assignment)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import os
import unittest
import HtmlTestRunner

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
# def test_sort_order_by_price(driver): 
#     driver.get("https://www.saucedemo.com/") 
#     driver.find_element(By.ID, "user-name").send_keys("standard_user") 
#     driver.find_element(By.ID, "password").send_keys("secret_sauce") 
#     driver.find_element(By.ID, "login-button").click() 
#     product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
#     products = [(product.find_element(By.CLASS_NAME, "inventory_item_name").text,
#                  float(product.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', ''))) 
#                  for product in product_elements] 
#     products.sort(key=lambda x: x[1]) 
#     prices = [price for _, price in products] 
#     assert prices == sorted(prices), "Prices are not sorted in ascending order" 
#     for name, price in products: print(f"{name}: ${price}")

#Lambda function : Anonymous function used to do small operations eg: 
# add = lambda x,y: x+y
# print(add(2,3)) #output : 5

#Exercise: Write a test case to log in to SauceDemo, navigate to the inventory page, and verify that the product names are correctly displayed. Generate an HTML report for the test results.
def test_verify_inventory_list(self):
    self.driver.get("https://www.saucedemo.com/") 
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user") 
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce") 
    self.driver.find_element(By.ID, "login-button").click() 
    inventory= self.driver.find_elements(By.CLASS_NAME,"inventory_list")
    list_of_products= ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                      'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
    product=[]
    for i in inventory:
        product_name = i.find_element(By.CLASS_NAME,"inventory_item_name").text
        product.append(product_name)
        
    assert product_name==list_of_products,"Name is not the same"
    #Screenshot
    screenshot_path = os.path.join(os.getcwd(), 'verify_product_name.png')
    screenshot_path = os.path.join(os.getcwd(), 'verify_product_name.png')
    try:
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
    except Exception as e:
        print(f"Error saving screenshot: {e}")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestSauceDemo('test_verify_inventory_list'))
    runner = HtmlTestRunner.HTMLTestRunner(output='reports')
    runner.run(suite)   

#Exercise : Add multiple items to the cart, verify the count on the cart. Remove the items and verify if the number on cart is getting updated.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
def test_cart_operations(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in add_buttons:
        button.click()
    
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == str(len(add_buttons)), "Cart count does not match the number of items added"  
    remove_buttons = driver.find_elements(By.CLASS_NAME, "btn_secondary")
    for button in remove_buttons:
        button.click()
    
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert not cart_badge, "Cart is not empty after removing items"
    
    print("Cart operations verified successfully")
if __name__ == "__main__":
    pytest.main(["-v", "--html=reports/cart.html"])

#Exercise : Write a test case to log in to SauceDemo, verify that all product images are loaded correctly by checking their src attributes and dimensions