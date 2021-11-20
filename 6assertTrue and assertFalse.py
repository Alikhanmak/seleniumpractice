import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome()
        driver.get("http://google.com/")

        titleOfWebPage = driver.title
        self.assertTrue(titleOfWebPage == "Google")


if __name__ == '__main__':
    unittest.main()