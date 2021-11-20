import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = {"python","selenium","java"}

        self.assertIn("python",list,"element not present") #True
        # self.assertNotIn("ruby", list, "element present") ##True


if __name__ == '__main__':
    unittest.main()
