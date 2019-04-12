from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.implicitly_wait(5)

# Checkbox Selection #

driver.get('https://projecteuler.net/register')
driver.maximize_window()

status = driver.find_element_by_id('privacy_accept').is_selected()
print(status)

driver.find_element_by_id('privacy_accept').click()

status1 = driver.find_element_by_id('privacy_accept').is_selected()
print(status1)

driver.close()
