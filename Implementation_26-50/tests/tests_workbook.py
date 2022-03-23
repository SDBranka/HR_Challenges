import unittest
import sys
sys.path.append("..")
from implementation import workbook


class test_workbook(unittest.TestCase):
    def testExampleCase(self):
        width = [2, 3, 2, 1]
        cases = [[1, 2], [2, 4]]
        self.assertEqual(workbook(n, k, arr), [2, 1])

    def testExampleCase(self):
        width = [2, 3, 1, 2, 3, 2, 3, 3]
        cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
        self.assertEqual(workbook(n, k, arr), [1, 2, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()       
