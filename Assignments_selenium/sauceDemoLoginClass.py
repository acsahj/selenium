import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
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

    
    #Test Case 2: Unsuccessful Login with Incorrect Username
    def test_login_wrongUsername(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("test1")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        self.assertEqual(expected_error, error_message, "Login error message does not match")
        screenshot_path = os.path.join(os.getcwd(), 'incorrect_username_login.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    #Test Case 3: Unsuccessful Login with Incorrect Password
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

    #Test Case 6: Sort Items by Price (Low to High) :Failing
    def test_sort_low_to_high(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        dropdown=self.driver.find_element(By.CLASS_NAME,"product_sort_container").click()
        dropdown.select_by_visible_text('Price (high to low)')
        #self.driver.find_element(By.CSS_SELECTOR,"Price (high to low)").click()
        screenshot_path = os.path.join(os.getcwd(), 'sort_high_to_low.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")


    #Test Case 7: Sort Items by Price (High to Low) :Failing
    def test_sort_low_to_high(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.driver.find_element(By.CLASS_NAME,"product_sort_container").click()
        self.driver.find_element(By.CSS_SELECTOR,"Price (high to low)").click()
        screenshot_path = os.path.join(os.getcwd(), 'sort_high_to_low.png')
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    
    #Test Case 8: Logout : Failing
    def test_logout(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        self.driver.find_element(By.ID,"logout_sidebar_link").click()
        assert(self.driver.find_element(By.CSS_SELECTOR,".btn_action").is_displayed())

    #Test Case 9: View Item Details
    def view_item_detailPage(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, ".btn_action").click()
        item_name= self.driver.find_element(By.CLASS_NAME,"inventory_item_name ").text
        description= self.driver.find_element(By.CLASS_NAME,"inventory_item_desc").text
        price= self.driver.find_element(By.CLASS_NAME,"inventory_item_price").text
        self.driver.find_element(By.ID,"item_4_img_link").click
        item_name_details_page= self.driver.find_element(By.CLASS_NAME,"inventory_details_name large_size").text
        item_description= self.driver.find_element(By.CLASS_NAME,"inventory_details_desc large_size").text
        item_price=self.driver.find_element(By.CLASS_NAME,"inventory_details_price").text

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestSauceDemo('test_login_wrongUsername'))
    # suite.addTest(TestSauceDemo('test_login'))
    # suite.addTest(TestSauceDemo('test_incorrect_password_login'))
    # suite.addTest(TestSauceDemo('test_add_to_cart'))
    # suite.addTest(TestSauceDemo('test_remove_from_cart'))
    # suite.addTest(TestSauceDemo('test_sort_low_to_high'))
    #suite.addTest(TestSauceDemo('test_logout'))
    suite.addTest(TestSauceDemo('view_item_detailPage'))
    runner = HtmlTestRunner.HTMLTestRunner(output='reports')
    runner.run(suite)










