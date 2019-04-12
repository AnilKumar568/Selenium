from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# 1. Scroll Down By Pixel
# driver.execute_script("window.scrollBy(0,1000)")

# 2. Scroll Down Page till the Element is visible
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[79]/td[1]/img')
driver.execute_script('arguments[0].scrollIntoView();', flag)

# 3. Scroll Down till the End of the Page
#driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')


driver.close()
