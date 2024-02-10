from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#Adding option for dont close browser untill automation
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://beta-web:8033/login")

username_field = driver.find_element(By.NAME, 'userName')
username_field.send_keys("FatanehBeta")
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('Alavi12345678911')

# EnterCaptcha
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

