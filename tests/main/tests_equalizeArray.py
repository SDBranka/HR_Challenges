import unittest
import sys
sys.path.append("../..")
from main import equalizeArray


class test_equalizeArray(unittest.TestCase):
    def testOne(self):
        self.assertEqual(equalizeArray([1, 2, 2, 3]), 2)

    def testTwo(self):
        self.assertEqual(equalizeArray([3, 3, 2, 1, 3]), 2)



if __name__ == '__main__':
    unittest.main()       