from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Navigational Commands #

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("http://www.python.org")
driver.maximize_window()  # Maximize the window #
# print(driver.title)  # it'll get the Title of the Page #
# print(driver.current_url)  # It'll return the current URL of the page #
# print(driver.page_source)  # It'll return the HTML code of the page #
assert 'Python' in driver.title
ele = driver.find_element_by_name("q")
ele.clear()
ele.send_keys("Pandas", Keys.RETURN)
assert 'No results found' not in driver.page_source
driver.close()
