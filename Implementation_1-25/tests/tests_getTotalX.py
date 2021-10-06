import unittest
import sys
sys.path.append("..")
from implementation import getTotalX


class test_getTotalX(unittest.TestCase):
    def testExample(self):
        a = [2, 6]
        b = [24, 36]
        self.assertEqual(getTotalX(a, b), 2)

    def testZero(self):
        a = [2, 4]
        b = [16, 32, 96]
        self.assertEqual(getTotalX(a, b), 2)


if __name__ == '__main__':
    unittest.main()       


    