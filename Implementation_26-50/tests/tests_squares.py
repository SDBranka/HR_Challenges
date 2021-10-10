import unittest
import sys
sys.path.append("..")
from implementation import squares


class test_squares(unittest.TestCase):
    def testExample(self):
        a, b = 24, 49
        self.assertEqual(squares(a, b), 3)

    def testZeroA(self):
        a, b = 3, 9
        self.assertEqual(squares(a, b), 2)

    def testZeroB(self):
        a, b = 17, 24
        self.assertEqual(squares(a, b), 0)

    def testThreeA(self):
        a, b = 178809602, 330598161
        self.assertEqual(squares(a, b), 4811)

    def testThreeB(self):
        a, b = 284829997, 636760792
        self.assertEqual(squares(a, b), 8358)


if __name__ == '__main__':
    unittest.main()       



# #6 Sherlock and Squares
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Watson likes to challenge Sherlock's math ability. 
# He will provide a starting and ending value that 
# describe a range of integers, inclusive of the 
# endpoints. Sherlock must determine the number of 
# square integers within that range.
# Note: A square integer is an integer which is the 
# square of an integer, e.g. 1, 4, 9, 16, 25.

# Example
# a = 24
# b = 49
# There are three square integers in the range: 25,
# 26, and 49. Return 3.

# Function Description
# Complete the squares function in the editor below. 
#   It should return an integer representing the 
#   number of square integers in the inclusive range 
#   from a to b.
# squares has the following parameter(s):
#     int a: the lower range boundary
#     int b: the upper range boundary

# Returns
#     int: the number of square integers in the range

# Input Format
# The first line contains q, the number of test cases.
# Each of the next q lines contains two space-separated 
# integers, a and b, the starting and ending integers 
# in the ranges.

# Constraints
#   1 <= q <= 100
#   1 <= a <= b <= 10^9

# Sample Input
# 2
# 3 9
# 17 24
# Sample Output
# 2
# 0
# Explanation
# Test Case #00: In range [3, 9], 4 and 9 are the two 
#   square integers.
# Test Case #01: In range [17, 24], there are no 
#   square integers. 

