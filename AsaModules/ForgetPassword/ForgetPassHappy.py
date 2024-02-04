from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from CRMmodules import Getsmspasscode

driver = webdriver.Chrome()
driver.get("http://beta-web:8033/login")
sleep(2)
ForgetPassword = driver.find_element(By.XPATH, "//button[contains(text(),'فراموشی کلمه عبور')]")
ForgetPassword.click()
sleep(5)
nationalCode = driver.find_element(By.XPATH, "//input[@name='nationalCode']")
nationalCode.send_keys("9524031949")
sleep(10)

#EnterCaptcha

SendKey = driver.find_element(By.XPATH, "//button[@type='submit']")
SendKey.click()
sleep(5)

sms_content = Getsmspasscode()
AuthenticateCode = driver.find_element(By.NAME, "authenticationCode")
AuthenticateCode.send_keys(sms_content)
sleep(2)
PassName = "Alavi12345678912"
newpassword = driver.find_element(By.NAME, "newPass").send_keys(PassName)
newpasswordconfirmation = driver.find_element(By.NAME, "newPassConfirmation").send_keys(PassName)
sleep(10)

#EnterCaptcha
#SubmitButton = driver.find_element(By.TAG_NAME, "button").find_element(By.CLASS_NAME, "btn btn-primary w-100 fs-16 align-c")
SubmitButton = driver.find_element(By.XPATH, "//button[@type='submit']")
SubmitButton.click()
sleep(3)

#Expected = driver.find_element(By.TAG_NAME,"p").find_element(By.CLASS_NAME, "border border-green green-bg-l green-c pd-10")
#Expected = driver.find_element(By.TAG_NAME, "tse-forgotten-password").find_element(By.TAG_NAME, 'div').find_element(By.TAG_NAME,'p').find_element(By.CLASS_NAME, "border border-green green-bg-l green-c pd-10")
Expected = driver.find_element(By.XPATH, "//p[@class='border border-green green-bg-l green-c pd-10']")
ExpectedMessage = Expected.text

sleep(5)
#print(ExpectedMessage)
ContainMessage = "FatanehBeta"
if ContainMessage in ExpectedMessage :
       print("TestPass")

driver.close()
driver.quit()






