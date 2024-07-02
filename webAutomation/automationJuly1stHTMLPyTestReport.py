#Two types of report generation : Pytest, HTML report
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner
class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_login_success(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        self.assertIn("inventory", driver.current_url)
        print("Login successful")
    
    def test_locked_out_user(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", error_message)
        print("Error message displayed correctly")

    @pytest.mark.medium
    def test_sort_products_by_price(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
        products = [(product.find_element(By.CLASS_NAME, "inventory_item_name").text,
                 float(product.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', '')))
                for product in product_elements]
        products.sort(key=lambda x: x[1])
        for name, price in products:
         print(f"{name}: ${price}")
        prices=[price for _,price in products]    
        assert prices == sorted(prices),"Prices are not sorted in ascending order"
        product = [
            ("product A",10.99),
            ("product B", 5.49),
        ]
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_title='SauceDemo Test Report',
        descriptions='Test Suite for Sauce Demo Application',
        add_timestamp=True
    ))

