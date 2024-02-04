from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://beta-web:8033/login")
sleep(2)
ForgetPasswordkey = driver.find_element(By.XPATH, "//button[contains(text(),'فراموشی کلمه عبور')]")
ForgetPasswordkey.click()
sleep(5)
#nationalcode = driver.find_element(By.NAME, "//input[@name='nationalCode']")
#nationalcode.send_keys("")

SendKey = driver.find_element(By.XPATH, "//button[@type='submit']")
SendKey.click()
sleep(2)
prompt = driver.find_element(By.XPATH, "//p[contains(text(),'لطفا کد ملی را وارد نمایید.')]")
PromptID = prompt.text

PromptMelli = 'ملی'

if PromptMelli in PromptID:
    print("TestPass")




