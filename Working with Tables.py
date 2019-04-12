from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()

# Scroll Down the page till the Table is found
scroll = driver.find_element_by_xpath('//*[@id="HTML1"]/h2')
driver.execute_script('arguments[0].scrollIntoView();', scroll)

# Data of Table will be stored in the <table>. <tr> represents row. <td> represents col.

num_rows = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr')) # Count No. of Rows. Took Xpath for tr
num_cols = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th'))   # Count No. of Cols. Took Xpath for td

print(num_rows)
print(num_cols)

print("BookName"+"         "+"Author"+"       "+"Subject"+"          "+"Price")

for r in range(2, num_rows+1): # 1st Row is header so we're starting with 2nd row. num_rows+1 bcz if we've 7 rows if i pass (2,7) it will not consider 7 till 6 it'll be checke
    for c in range(1, num_cols+1):
        val = driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']') # I took the Xpath of values i.e 1st row & 1st col data. Inorder to apply for all the rows & cols we're replacing with r & c values
        for data in val:
            print(data.text, end='  ')
    print()

"""
When i use the below code i've encountered with an error 'list' object has no attribute 'text'.
for r in range(2,num_rows+1):
    for c in range(1, num_cols+1):
        val = driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(val.text, end='  ')
    print()
"""