# It's Not Working Take a Look into It

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://test-usg-ui.reltio.com/ui/xr8Cd2cfKDejJ2u')

ele = driver.find_element_by_name("username")
ele.clear()
ele.send_keys('UCBIMS1_TEST_API_USER')


