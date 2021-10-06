import unittest
import sys
sys.path.append("..")
from implementation import migratoryBirds


class test_migratoryBirds(unittest.TestCase):
    def testExample(self):
        arr = [1, 1, 2, 2, 3]
        self.assertEqual(migratoryBirds(arr), 1)

    def testZero(self):
        arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
        self.assertEqual(migratoryBirds(arr), 3)


if __name__ == '__main__':
    unittest.main()       

