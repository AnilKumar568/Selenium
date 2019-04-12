from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://demo.automationtesting.in/FileUpload.html')
driver.maximize_window()

# driver.switch_to_frame(0)

driver.find_element_by_xpath('//*[@id="input-4"]').send_keys('C://Users/Akumar4/Desktop/Test.txt')
