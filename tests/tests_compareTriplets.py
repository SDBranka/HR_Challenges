import unittest
import sys
sys.path.append("..")
from warmup_challenges import compareTriplets

class test_compareTriplets(unittest.TestCase):
    def testOne(self):
        a = [1, 2, 3]
        b = [3, 2, 1]
        self.assertEqual(compareTriplets(a, b), [1, 1])

    def testTwo(self):
        a = [5, 6, 7]
        b = [3, 6, 10]
        self.assertEqual(compareTriplets(a, b), [1, 1])






if __name__ == '__main__':
    unittest.main()       