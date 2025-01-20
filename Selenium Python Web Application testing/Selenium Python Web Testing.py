# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver (ensure chromedriver.exe is in PATH)
driver = webdriver.Chrome("chromedriver.exe")

# Open a local HTML file
driver.get("file:///C:/Users/User.user/source/repos/1.%20Website/homepage.html")
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Click a link identified by partial text
phishing_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Phishing")
phishing_link.click()

# Fill out an email field (replace with correct field name or id)
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("joebloggs@email.com")

# Optionally, simulate pressing Enter
email_field.send_keys(Keys.RETURN)

# Keep the browser open for observation
time.sleep(5)

# Close the browser
driver.quit()
