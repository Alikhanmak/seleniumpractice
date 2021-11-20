import unittest


class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup ny email test")
        self.assertTrue(True)  # add assertion here

    def test_signupbyFacebook(self):
        print("This is signup ny facebook test")
        self.assertTrue(True)  # add assertion here

    def test_signupbyTwitter(self):
        print("This is signup ny twitter test")
        self.assertTrue(True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
