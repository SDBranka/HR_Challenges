import unittest
import sys
sys.path.append("..")
from implementation import extraLongFactorials


class test_extraLongFactorials(unittest.TestCase):
    def testExample(self):
        n = 30
        self.assertEqual(extraLongFactorials(n), 265252859812191058636308480000000)

    def testZero(self):
        n = 25
        self.assertEqual(extraLongFactorials(n), 15511210043330985984000000)

    def testOne(self):
        n = 45
        self.assertEqual(extraLongFactorials(n), 119622220865480194561963161495657715064383733760000000000)


if __name__ == '__main__':
    unittest.main()       



# #29 Extra Long Factorials
# https://www.hackerrank.com/challenges/extra-long-factorials/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# The factorial of the integer n, written n!, is 
# defined as:
#       n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
# Calculate and print the factorial of a given integer.
# For example, if n = 30, we calculate 
# 30 * 29 * 28 * ... * 2 * 1  and get:
# 265252859812191058636308480000000

# Function Description
# Complete the extraLongFactorials function in the editor below. It should print the result and return.
# extraLongFactorials has the following parameter(s):
#     n: an integer
# Note: Factorials of n > 20 can't be stored even in
# a 64 -bit long long variable. Big integers must be 
# used for such calculations. Languages like Java, 
# Python, Ruby etc. can handle big integers, but we 
# need to write additional code in C/C++ to handle 
# huge values.
# We recommend solving this challenge using 
# BigIntegers.

# Input Format
# Input consists of a single integer n

# Constraints
#   1 <= n <= 100

# Output Format
# Print the factorial of n.

# Sample Input
# n = 25
# Sample Output
# 15511210043330985984000000
# Explanation
# 25! = 25*24...*3*2*1
