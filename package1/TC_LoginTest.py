import unittest


class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login ny email test")
        self.assertTrue(True)  # add assertion here

    def test_loginbyFacebook(self):
        print("This is login ny facebook test")
        self.assertTrue(True)  # add assertion here

    def test_loginbyTwitter(self):
        print("This is login ny twitter test")
        self.assertTrue(True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
