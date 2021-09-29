import unittest
import sys
sys.path.append("../..")
from implementation import kangaroo


class test_kangaroo(unittest.TestCase):
    def testExample(self):
        x1 = 2
        v1 = 1
        x2 = 1
        v2 = 2
        self.assertEqual(kangaroo(x1, v1, x2, v2), "YES" )

    def testZero(self):
        x1 = 0
        v1 = 3
        x2 = 4
        v2 = 2
        self.assertEqual(kangaroo(x1, v1, x2, v2),"YES" )

    def testOne(self):
        x1 = 0
        v1 = 2
        x2 = 5
        v2 = 3
        self.assertEqual(kangaroo(x1, v1, x2, v2), "NO")



if __name__ == '__main__':
    unittest.main()       