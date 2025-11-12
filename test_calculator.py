import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -8), -8)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 4), 1)
        self.assertEqual(subtract(7, 9)), -2)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(5,5), 25)
        self.assertEqual(multiply(100,6), 600)
        self.assertEqual(multiply(100000,1),100000)


    def test_divide(self): # 3 assertions
        self.assertEqual(divide(50,5),10)
        self.assertEqual(divide(100000,1), 100000)
        self.assertEqual(divide(5,5),1)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #div(0, 5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 4), 2)
        self.assertEqual(log(-2, -8), 3)
        self.assertEqual(log(5, 5), 1)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        self.assertRaises(ZeroDivisionError, log, 5, 0)
    

     def test_log_invalid_argument(self): # 1 assertion
         self.assertRaises(log(-1,5),ValueError)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4,3),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(6,8),10)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(sqrt(0), ValueError)
        self.assertEqual(sqrt(25),5)
        self.assertEqual(sqrt(100),10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()