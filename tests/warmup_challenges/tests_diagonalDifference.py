import unittest
import sys
sys.path.append("../..")
from warmup_challenges import diagonalDifference


class test_diagonalDifference(unittest.TestCase):
    def testOne(self):
        arr = [[11, 2, 4],
                [4, 5, 6],
                [10, 8, -12]
        ]   
        self.assertEqual(diagonalDifference(arr), 15)

    def testTwo(self):
        arr = [[1, 2, 3],
                [4, 5, 6],
                [9, 8, 9]  
                ]
        self.assertEqual(diagonalDifference(arr), 2)



if __name__ == '__main__':
    unittest.main()       