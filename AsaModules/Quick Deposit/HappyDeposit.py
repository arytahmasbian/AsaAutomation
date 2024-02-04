from selenium import webdriver
from selenium.webdriver.common.by import By
from AsaModules.RefrenceModules.LoginModuleRef import LoginModuleRef

driver = webdriver.Chrome()
LoginModuleRef()
#LoginModuleRef page = PageFactory.intElements(driver,LoginModuleRef().class)

BranchOpen = driver.find_element(By.TAG_NAME, "div").find_element(By.CLASS_NAME, "app-menu pd-r-10 c-pointer p-relative z-1")
BranchOpen.click()

DepositItem = driver.find_element(By.XPATH, "//a[@role='menuitem']//span[@class='p-menuitem-text ng-star-inserted'][contains(text(),'پرداخت شتابی')]")

