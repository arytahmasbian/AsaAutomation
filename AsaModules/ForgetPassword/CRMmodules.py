from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


def Getsmspasscode():
    driver = webdriver.Chrome()

    driver.get("http://betacrm.asax.local/#/Dashboard")

    username_field = driver.find_element(By.ID, 'username')
    sleep(1)
    username_field.send_keys("s.ghafari")
    sleep(2)
    password_field = driver.find_element(By.ID, 'password')
    sleep(2)
    password_field.send_keys('admin')
    sleep(10)

    # EnterCaptcha

    SubmitButton = driver.find_element(By.XPATH, "//button[@type='submit']")
    SubmitButton.click()
    sleep(5)
    MessagePlus = driver.find_element(By.XPATH, "//li[contains(text(),'پیامک پلاس')]")
    MessagePlus.click()
    sleep(2)
    SentMessage = driver.find_element(By.XPATH, "//a[@ng-href='#/ucPlus/sms/sentSms']")
    SentMessage.click()
    sleep(2)
    driver.find_element(By.XPATH, "//i[@class='iconFilter']").click()
    sleep(2)
    SearchItem = driver.find_element(By.XPATH, "//table[@class='table ng-scope ng-table sticky-enabled']//th[4]//div[1]//div[1]//div[1]//input[1]")
    SearchItem.send_keys("09104041465")
    SearchItem.send_keys(Keys.ENTER)
    sleep(2)

    driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/i[1]").click()
    sleep(2)

    # contentMessage = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td").text
    contentMessage = \
    driver.find_element(By.CLASS_NAME, "loadingContainer").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME,
                                                                                                            "tr")[
        1].find_element(By.CLASS_NAME, "ng-binding").text
    sended_code = contentMessage[-8:]

    return sended_code
