from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

"""
Inorder to download a file in the above website need to enter details in the provided text box then Generate button will be Enabled.
Click on Generate, Download link will be avail for downloading data in a Text file. Similarly for PDF.
"""


driver.find_element_by_id('textbox').send_keys('Download the Text file')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_xpath('//*[@id="link-to-download"]').click()


