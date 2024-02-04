from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://beta-web:8033/login")

sleep(2)
username_field = driver.find_element(By.NAME, 'userName')
sleep(1)
username_field.send_keys("AAAA")
sleep(2)
password_field = driver.find_element(By.NAME, 'password')
sleep(2)
password_field.send_keys('Alavi12345678911')
sleep(10)


login_button = driver.find_element(*(By.XPATH, "//button[@type='submit']"))
login_button.click()
sleep(5)


#toast_container_element = driver.find_element(By.XPATH, '//*[@id="toast-container"]/div/div[1]')
toast_container_element = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
element_text = toast_container_element.text

sleep(5)
sample = "اشتباه"

if sample in element_text:
     print("TestPass")
else:
    print("TestFail")

driver.quit()





