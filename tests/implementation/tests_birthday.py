import unittest
import sys
sys.path.append("../..")
from implementation import birthday


class test_birthday(unittest.TestCase):
    def testExample(self):
        s = [2, 2, 1, 3, 2]
        d = 4
        m = 2
        self.assertEqual(birthday(s, d, m), 2)

    def testZero(self):
        s = [1, 2, 1, 3, 2]
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m), 2)

    def testOne(self):
        s = [1, 1, 1, 1, 1, 1]
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m), 0)

    def testTwo(self):
        s = [4]
        d = 4
        m = 1
        self.assertEqual(birthday(s, d, m), 1)

    def testThree(self):
        s = [2, 5, 1, 3, 4, 4, 3,       
            5, 1, 1, 2, 1, 4, 1,        
            3, 3, 4, 2, 1]
        d = 18
        m = 7
        self.assertEqual(birthday(s, d, m), 3)

    def testThree(self):
        s = [2, 2]
        d = 4
        m = 8
        self.assertEqual(birthday(s, d, m), 1)



if __name__ == '__main__':
    unittest.main()       