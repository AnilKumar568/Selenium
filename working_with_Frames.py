# Getting Errors take a better website and check #
from selenium import webdriver
# from selenium.webdriver.common.by import By #
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://the-internet.herokuapp.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_link_text('Frames').click()
driver.find_element_by_link_text('Nested Frames').click()
driver.switch_to.frame('frame-left')
"""
# Now you're in Left frame. Here you can perform actions like click, selections etc. After clicking on the link you can not directly shift to other frames #
# page contains frames. So after clicking on a link in left frame you need to go back to Page by using driver.switch_to.default_content() and then you can switch to other frames #
"""
driver.switch_to.default_content()
driver.switch_to.frame('frame-middle')
driver.switch_to.default_content()
driver.switch_to.frame('frame-right')
driver.switch_to.default_content()
driver.switch_to.frame('frame-bottom')
driver.switch_to.default_content()

driver.close()
