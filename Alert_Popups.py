from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)

alert = driver.switch_to.alert
alert.dismiss()

"""
or
# alert = Alert(driver) # # to use this you need to import from selenium.webdriver.common.alert import Alert #
# alert.accept() #
"""

# driver.switch_to_alert().accept() # # switch_to_alert() is depricated #

driver.close()