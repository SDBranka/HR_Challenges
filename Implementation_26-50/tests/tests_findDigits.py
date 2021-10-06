import unittest
import sys
sys.path.append("..")
from implementation import findDigits


class test_findDigits(unittest.TestCase):
    def testExampleA(self):
        n = 124
        self.assertEqual(findDigits(n), 3)

    def testExampleB(self):
        n = 111
        self.assertEqual(findDigits(n), 3)

    def testExampleC(self):
        n = 10
        self.assertEqual(findDigits(n), 1)

    def testZeroA(self):
        n = 12
        self.assertEqual(findDigits(n), 2)

    def testZeroB(self):
        n = 1012
        self.assertEqual(findDigits(n), 3)


if __name__ == '__main__':
    unittest.main()       



# #3 Find Digits
# https://www.hackerrank.com/challenges/find-digits/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# An integer d is a divisor of an integer n if the 
# remainder of n / d == 0.
# Given an integer, for each digit that makes up the 
# integer determine whether it is a divisor. Count the
# number of divisors occurring within the integer.

# Example
# n = 124
# Check whether 1, 2 and 4 are divisors of 124. All 
# 3 numbers divide evenly into so return 3.
# n = 111
# Check whether 1, 1, and 1 are divisors of 111. All
# 3 numbers divide evenly into so return 3.
# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but
# 0 is not. Return 1.

# Function Description
# Complete the findDigits function in the editor below.
# findDigits has the following parameter(s):
#     int n: the value to analyze

# Returns
#     int: the number of digits in n that are 
#           divisors of n

# Input Format
# The first line is an integer, t, the number of test
#   cases.
# The t subsequent lines each contain an integer, n.

# Constraints
#   1 <= t <= 15
#   0 < n < 10^9

# Sample Input
# 2
# 12
# 1012
# Sample Output
# 2
# 3
# Explanation
# The number 12 is broken into two digits, 1 and 2. 
# When 12 is divided by either of those two digits, 
# the remainder is 0 so they are both divisors.
# The number 1012 is broken into four digits, 1, 0, 1,
# and 2. 1012 is evenly divisible by its digits 1, 1,
# and 2, but it is not divisible by 0 as division by 
# zero is undefined.