from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get("https://psfmember.org/civicrm/contribute/transact?reset=1&id=13")
time.sleep(5)
driver.maximize_window()
ele = driver.find_element_by_xpath('//*[@id="CIVICRM_QFID_1_payment_processor"]')

# For Radio button #

print(ele.is_selected())
print(ele.is_displayed())
print(ele.is_enabled())

driver.close()