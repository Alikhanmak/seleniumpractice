import unittest

class SetUpAndTearDown(unittest.TestCase):


    @classmethod
    def setUp(self):
        print("This is login test")#this will run before every test method

    @classmethod
    def tearDown(self):
        print("This is logout test")#this will run after every test method

    @classmethod
    def setUpClass(cls):
        print("open application")  # this will run only once before test methods

    @classmethod
    def tearDownClass(cls):
        print("close application")#this will run only once after test methods


    def test_checkHi(self):
        print("Yes HIIII is present")

if __name__ == "__main__":
    unittest.main()
