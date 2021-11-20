import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertGreater(100,10)
        self.assertGreater(100, 100)
        self.assertLess(10, 100)
        self.assertLessEqual(100, 100)



if __name__ == '__main__':
    unittest.main()
