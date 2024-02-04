from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://beta-web:8033/login")

sleep(2)
#driver.find_element(By.TAG_NAME, "username").send_keys("A14617168")
#sleep(5)
#driver.find_elements(By.TAG_NAME, "password")[0].send_keys("vw3fc3qq")

username_field = driver.find_element(By.XPATH,"//form/div/label[1]/input")
sleep(3)
#username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys('FatanehBeta')
sleep(3)
password_field = driver.find_element(By.NAME, 'password')

# Enter the username and password

password_field.send_keys('Alavi1234567891')


sleep(3)
#driver.find_elements(By.CSS_SELECTOR, "type.submit")[0].click()
login_button = driver.find_element(By.XPATH, "//tse-login/form/div/div/button")
login_button.click()

sleep(3)
element_to_compare = driver.find_element(By.XPATH, "//label[3]/arv-validation-messages/div/div/p")
element_text = element_to_compare.text

expected_text ="لطفا کد کپچا را وارد کنید."
if expected_text == element_text:
    print("TestPass")

driver.quit()
