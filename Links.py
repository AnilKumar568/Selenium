from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://the-internet.herokuapp.com/')

links = driver.find_elements_by_tag_name('a')

# 1. How many Links are present #
print(len(links))

"""
# 2. Capture links #
for x in links:
    print(x.text)
"""

# 3.Click on the Links: Link Text & Partial Link Text #

# driver.find_element_by_link_text('Exit Intent').click() #
driver.find_element_by_partial_link_text('ex')

time.sleep(10)
driver.close()
