from selenium import  webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
driver.maximize_window()

# driver.save_screenshot(r'C:\Users\Akumar4\Desktop\screenshot.jpg') # Give the Path & filename

driver.get_screenshot_as_file(r'C:\Users\Akumar4\Desktop\screenshot2.png')

driver.close()

