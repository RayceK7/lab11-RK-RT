# https://github.com/RayceK7/lab11-RK-RT
#Partner 1: Rayce Kronenberg
#Partner 2: Ragul Thiyagarajan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    

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