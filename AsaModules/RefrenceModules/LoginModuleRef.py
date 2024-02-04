from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def LoginModuleRef():
    driver = webdriver.Chrome()
    driver.get("http://beta-web:8033/login")
    sleep(2)
    # username_field = driver.find_element(By.XPATH, "//form/div/label[1]/input")
    username_field = driver.find_element(By.NAME, 'userName')

    sleep(1)
    username_field.send_keys("FatanehBeta")
    sleep(2)
    password_field = driver.find_element(By.NAME, 'password')
    sleep(2)
    password_field.send_keys('Alavi12345678911')
    sleep(10)

    # EnterCaptcha

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(5)

