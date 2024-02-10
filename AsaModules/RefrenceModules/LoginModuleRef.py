from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def LoginModuleRef():
    # Adding option for don't close browser until automation
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://beta-web:8033/login")
    sleep(3)
    # username_field = driver.find_element(By.XPATH, "//form/div/label[1]/input")
    username_field = driver.find_element(By.NAME, 'userName')
    sleep(3)
    username_field.send_keys("FatanehBeta")
    password_field = driver.find_element(By.NAME, 'password')
    sleep(3)
    password_field.send_keys('Alavi12345678911')
    # Enter Captcha
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
