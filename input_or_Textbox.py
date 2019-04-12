from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.implicitly_wait(5)

driver.get('https://www.formsite.com/')
driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[3]/div[3]/a').click()

# 1. How to find how many textboxes are available in the webpage #

inputbox = driver.find_elements(By.CLASS_NAME, 'auth-form__text-input')
print(len(inputbox))

# 2. How to provide value into the textbox #

driver.find_element_by_id('UserId').send_keys('anil')
driver.find_element_by_id('Password1').send_keys('kumar')

# 3. How to get the status #
status = driver.find_element_by_id('UserId').is_displayed()
print(status)

status1 = driver.find_element_by_id('Password1').is_enabled()
print(status1)


driver.close()