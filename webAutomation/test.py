from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Launch a webpage
driver.get("https://www.google.com")

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()

#Assignment : Test cases for login process

