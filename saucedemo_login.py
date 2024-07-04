from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
import os

username = "standard_user"
password = "secret_sauce"

# driver_path = os.getenv("Path")
driver_path2 = r"C:\Users\Bony_\Drivers\chromedriver-win64\chromedriver.exe"

driver = Chrome(service=Service(driver_path2))
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys(username)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

print(driver.current_url == "https://www.saucedemo.com/inventory.html")

sleep(2)
driver.quit()
