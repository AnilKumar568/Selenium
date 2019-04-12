from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://demo.automationtesting.in/Windows.html')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle) # CDwindow-05B56FF9CB57B7C5749D2247010FB05E - This will display the current window #

handles = driver.window_handles # Returns all the handle values of opened browser windows #

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()

driver.quit() # It'll close all the opened windows # driver.close() is used to closed only particular window


