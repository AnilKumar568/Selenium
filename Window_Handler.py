from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://the-internet.herokuapp.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_link_text('Multiple Windows').click()

print(driver.current_window_handle) # Parent Window #

handles = driver.window_handles  # Return all the handle values of opened browser windows #

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.close()
