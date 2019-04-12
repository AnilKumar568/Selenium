import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://www.google.co.in')
        print(self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Akumar4\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://www.bing.com')
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
