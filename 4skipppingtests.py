import unittest

class testing(unittest.TestCase):


    @unittest.SkipTest #Thhis will skip the next method
    def test_search(self):
        print("This is a search test")


    @unittest.skip("NOt implimented yet")#this will give the message in the quotations
    def test_advancedsearch(self):
        print("This is advanced search")

    def test_prepaidrecharge(self):
        print("this is prepaid ")

    def test_postpaid(self):
        print("this is postpaid")

if __name__ == "__main__":
    unittest.main()