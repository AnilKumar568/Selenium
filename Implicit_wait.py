from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')
'''
driver.implicitly_wait(8)  # Implicitly wait is applicable for all the pages #
driver.get('https://www.flipkart.com/search?q=motorola+mobiles&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_8&otracker1=AS_Query_OrganicAutoSuggest_1_8&as-pos=1&as-type=RECENT&as-searchtext=motorola')
driver.maximize_window()
'''

driver.implicitly_wait(10)
driver.get('https://www.expedia.com/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="tab-flight-tab-hp"]').click()
ele = driver.find_element_by_xpath('//*[@id="flight-origin-hp-flight"]')
ele.clear()
ele.send_keys("Bangalore")

ele2 = driver.find_element_by_xpath('//*[@id="flight-destination-hp-flight"]')
ele2.clear()
ele2.send_keys("Delhi")

time.sleep(10)

ele3 = driver.find_element_by_xpath('//*[@id="flight-departing-hp-flight"]')
ele3.clear()
ele3.send_keys('02/03/2019')


time.sleep(5)

driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

time.sleep(10)

driver.close()
