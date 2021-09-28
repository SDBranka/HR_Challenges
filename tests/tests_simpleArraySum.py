import unittest
import sys
sys.path.append("..")
from warmup_challenges import simpleArraySum

class test_simpleArraySum(unittest.TestCase):
    def testOne(self):
        ar = [1, 2, 3]
        self.assertEqual(simpleArraySum(ar), 6)

    def testTwo(self):
        ar = [1, 2, 3, 4, 10, 11]
        self.assertEqual(simpleArraySum(ar), 31)





if __name__ == '__main__':
    unittest.main()       