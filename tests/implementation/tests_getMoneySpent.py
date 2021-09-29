import unittest
import sys
sys.path.append("../..")
from implementation import getMoneySpent


class test_getMoneySpent(unittest.TestCase):
    def testOne(self):
        b = 60
        keyboards = [40, 50, 60]
        drives = [5, 8, 12]
        self.assertEqual(getMoneySpent(keyboards, drives, b), 58)

    def testTwo(self):
        b = 10
        keyboards = [3, 1]
        drives = [5, 2, 8]
        self.assertEqual(getMoneySpent(keyboards, drives, b), 9)

    def testThree(self):
        b = 5
        keyboards = [4]
        drives = [5]
        self.assertEqual(getMoneySpent(keyboards, drives, b), -1)



if __name__ == '__main__':
    unittest.main()       