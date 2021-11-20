import unittest
from selenium import webdriver

class Test (unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("http://www.google.com/")
        titleOfWebPage = driver.title

        #assertEqual

        self.assertEqual("Google",titleOfWebPage,"webpage title is not same as mentioned")

        #asserNotEqual

        #self.assertNotEqual("Google123",titleOfWebPage,"webpage title are same")


if __name__ == "__main__":
    unittest.main()