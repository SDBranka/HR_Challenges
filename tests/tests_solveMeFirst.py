import unittest
import sys
sys.path.append("..")
from warmup_challenges import solveMeFirst

class test_solveMeFirst(unittest.TestCase):
    def testOne(self):
        a = 7
        b = 3
        self.assertEqual(solveMeFirst(a, b), 10)

    def testTwo(self):
        a = 2
        b = 3
        self.assertEqual(solveMeFirst(a, b), 5)





if __name__ == '__main__':
    unittest.main()       