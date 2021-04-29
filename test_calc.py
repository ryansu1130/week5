import unittest
import calc
import math

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(calc.addition(5,5),10)

    def testTwo(self):
        self.assertEqual(calc.addition(5,10),10)

    def testThree(self):
        self.assertEqual(calc.subtraction(-5,-5),0)

    def testFour(self):
        self.assertEqual(calc.subtraction(100,0),10)

    def testFive(self):
        self.assertEqual(calc.multiplication(2,100),200)

    def testSix(self):
        self.assertEqual(calc.multiplication(1,5),10)

    def testSeven(self):
        self.assertEqual(calc.division(0,5),0)

    def testEight(self):
        '''Can not divide by zero'''
        self.assertNotEqual(calc.division(5.0),0)

if __name__ == '__main__':
    unittest.main()
