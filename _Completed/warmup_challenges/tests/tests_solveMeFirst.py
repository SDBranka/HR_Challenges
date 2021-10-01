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



# #1 Solve Me First
# https://www.hackerrank.com/challenges/solve-me-first/problem
# Complete the function solveMeFirst to compute
#  the sum of two integers.

# Example
# a = 7
# b = 3
# Return
# 10

# Function Description
# Complete the solveMeFirst function in the editor below.
# solveMeFirst has the following parameters:
#     int a: the first value
#     int b: the second value

# Returns
# - int: the sum of a and b

# Constraints
# 1 <= a, b <= 1000
# Sample Input
# a = 2
# b = 3
# Sample Output
# 5
# Explanation
# 2 + 3 = 5. 
