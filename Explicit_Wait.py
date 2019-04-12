from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.expedia.com/')
driver.maximize_window()

try:
    # path = '//*[@id="reasons-to-believe-banner"]/li[1]/span[2]' #
    wait = WebDriverWait(driver, 10)
    # ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))#
    # ele = wait.until(EC.title_is('Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations')) #
    ele = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-account-menu"]')))

finally:
    driver.quit()


