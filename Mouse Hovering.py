from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')
"""
#1. Mouse Hover
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]')
usermgt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
user = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

actions = ActionChains(driver)  # Create an Object 'actions' for ActionChains class

actions.move_to_element(admin).move_to_element(usermgt).move_to_element(user).click().perform()

time.sleep(10)

driver.close()
"""

"""
# 2. Double Click

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

ele = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button').click()

actions = ActionChains(driver)
actions.double_click(ele).perform()

time.sleep(10)

driver.close()
"""

"""
# 3. Right Click:

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# Scroll Don till the Ele is found

flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[79]/td[1]/img')
driver.execute_script('arguments[0].scrollIntoView();', flag)

driver.implicitly_wait(5)

actions = ActionChains(driver)

# Perform Right click by using context_click()
actions.context_click(flag).perform()

"""

"""

# 4. Drag & Drop:

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

src = driver.find_element_by_xpath('//*[@id="gallery"]/li[1]/img')
target = driver.find_element_by_xpath('//*[@id="trash"]')

driver.execute_script('arguments[0].scrollIntoView();', src)

actions = ActionChains(driver)

actions.drag_and_drop(src, target).perform()

"""
