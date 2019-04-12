# It didn't workded as expected. Give a Try again

from selenium import webdriver

# In Chrome if you click on Download button automatically file gets downloaded. It is not the same case in the Firefox browser.
# A window will be popped up. So we can set Preferences to avoid this in Firefox. In chrome we call it has options.

fp = webdriver.FirefoxProfile()  # creating an Object

fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain,application/pdf')
# 'browser.helperApps.neverAsk.saveToDisk' - It'll not ask you to save to disk. Window will be disabled
# 'text/plain,application/pdf' - These are Mime Type. File can be Text,PDF etc

fp.set_preference('browser.download.manager.showWhenStarting', False) # Download Progress
fp.set_preference('browser.download.dir', r'C:\Users\Akumar4\Downloads\Download')  # Downloading files in the desired dir
fp.set_preference('browser.download.folderlist', 2)  # 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory
# fp.set_preference('pdfjs.disabled', True)  # PDF file would be downloaded automatically

driver = webdriver.Firefox(executable_path=r'C:\Users\Akumar4\Downloads\geckodriver.exe')

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

"""
Inorder to download a file in the above website need to enter details in the provided text box then Generate button will be Enabled.
Click on Generate, Download link will be avail for downloading data in a Text file. Similarly for PDF.
"""


driver.find_element_by_id('textbox').send_keys('Download the Text file')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_xpath('//*[@id="link-to-download"]').click()


