import unittest
from selenium import webdriver



class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome()
        self.assertIsNone(driver,msg="driver object is not none")
        # driver.get("http://google.com/")





if __name__ == '__main__':
    unittest.main()
