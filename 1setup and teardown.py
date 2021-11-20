import unittest

class SetUpAndTearDown(unittest.TestCase):


    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")


    def test_checkHi(self):
        print("Yes HIIII is present")

if __name__ == "__main__":
    unittest.main()
