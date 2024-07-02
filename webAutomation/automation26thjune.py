#Handling multiple windows
#Taking Screenshots

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.execute_script("window.open('https://www.example.com','_blank');")
# driver.execute_script("window.open('https://www.python.org','_blank');")

# #Close tab with URL with https://www.example.com
# for window in driver.window_handles:
#     driver.switch_to.window(window)
#     if driver.current_url=="https://www.example.com":
#         driver.close()
# driver.quit()

#Firefox : Close the tab and get the title of the current tab
# driver=webdriver.Firefox()
# original_window=driver.current_window_handle
# driver.get("https://www.saucedemo.com")
# driver.execute_script("window.open('https://www.example.com','_blank');")
# time.sleep(2)
# new_window=[window for window in driver.window_handles if window!=original_window][0]
# driver.switch_to.window(new_window)
# driver.close()
# driver.switch_to.window(original_window)
# time.sleep(2)
# print(f'Page Title: {driver.title}')

#driver.window_handles:This is a list of the handles (identifiers) of all the open windows or tabs that the WebDriver is aware of. Each window or tab opened by the WebDriver gets a unique handle.

#Exercise : Open three tabs and print the title of each tab.

# driver=webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# original_window=driver.current_window_handle
# driver.execute_script("window.open('https://www.python.org','_blank');")
# driver.execute_script("window.open('https://www.saucedemo.com','_blank');")
# driver.execute_script("window.open('https://www.selenium.dev','_blank');")
# time.sleep(2)
# windows=driver.window_handles
# for window in windows :
#     driver.switch_to.window(window)
#     print(f"Tab Tile : {driver.title}")

#Exercise: Write a script to open two new tabs, switch back to the original tab, and print the URL.

# driver=webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# original_window=driver.current_window_handle
# driver.execute_script("window.open('https://www.python.org','_blank');")
# driver.switch_to.window(original_window)
# print(f"Current URL : {driver.current_url}")

# #################################################Screenshots############################################
# #Screenshot of the whole screen
# driver=webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# driver.save_screenshot("screenhot3.png")

#Screenshot a particular element
# driver=webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# element=driver.find_element(By.ID,"login-button")
# element.screenshot("Login.png")

# #Screenshot for each step
# driver=webdriver.Firefox()
# driver.get("https://www.saucedemo.com/")
# driver.save_screenshot("report_screenshot2.png")
# with open("report2.html","w") as report:
#     report.write("<h1>Test Report on Saucedemo<h1>")
#     report.write('<img src="report_screenshot2.png" alt="Screenhot">')

#Write a script to navigate to SauceDemo, log in, and take a screenshot of the inventory page
driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.save_screenshot("inventory_screenshot.png")
with open("report2.html","w") as report:
    report.write("<h1>Test Report on Saucedemo<h1>")
    report.write('<img src="inventory_screenshot.png" alt="Screenhot">')



