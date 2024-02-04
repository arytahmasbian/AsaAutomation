from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://beta-web:8033/login")
sleep(2)
ForgetPassword = driver.find_element(By.XPATH, "//button[contains(text(),'فراموشی کلمه عبور')]")
ForgetPassword.click()
sleep(5)
nationalCode = driver.find_element(By.XPATH, "//input[@name='nationalCode']")
nationalCode.send_keys("1292047399")
sleep(2)
SendKey = driver.find_element(By.XPATH, "//button[@type='submit']")
SendKey.click()
sleep(2)
prompt = driver.find_element(By.XPATH, "//p[contains(text(),'لطفا کد کپچا را وارد نمایید.')]")
PromptID = prompt.text

PromptMelli = 'کد کپچا'

if PromptMelli in PromptID:
    print("TestPass")
