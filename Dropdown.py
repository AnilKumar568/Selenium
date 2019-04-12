from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.implicitly_wait(5)
driver.get('http://the-internet.herokuapp.com/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="content"]/ul/li[9]/a').click()

drp = Select(driver.find_element_by_id('dropdown'))

# 1. Select an Option #
# drp.select_by_visible_text('Option 2') #
# drp.select_by_index(1) #
#drp.select_by_value('2')

# 2. Count How many options are present #

print(len(drp.options))

# 3 Find out how many options present in Dropdown #

all_options = drp.options
for x in all_options:
    print(x.text)




time.sleep(10)

driver.close()