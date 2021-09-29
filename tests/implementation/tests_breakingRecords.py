import unittest
import sys
sys.path.append("../..")
from implementation import breakingRecords


class test_breakingRecords(unittest.TestCase):
    def testExample(self):
        scores = [12, 24, 10, 24]
        self.assertEqual(breakingRecords(scores), [1, 1])

    def testZero(self):
        scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        self.assertEqual(breakingRecords(scores), [2, 4])

    def testOne(self):
        scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
        self.assertEqual(breakingRecords(scores), [4, 0])



if __name__ == '__main__':
    unittest.main()       