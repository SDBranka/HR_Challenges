import io
import unittest
import unittest.mock
import sys
sys.path.append("..")
from warmup_challenges import plusMinus


class test_simpleArraySum(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        plusMinus(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 1, 0, -1, -1]
        self.assert_stdout(arr, "0.400000\n0.400000\n0.200000\n")

    def testTwo(self):
        arr = [-4, 3, -9, 0, 4, 1]
        self.assertEqual(arr, "0.500000\n0.333333\n0.166667\n")

    def testThree(self):
        arr = [1, 2, 3, -1, -2, -3, 0, 0]
        self.assertEqual(arr, "0.375000\n0.375000\n0.250000")


if __name__ == '__main__':
    unittest.main()       



# #6 Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given an array of integers, calculate the ratios of its 
# elements that are positive, negative, and zero. Print the 
# decimal value of each fraction on a new line with 6 places
# after the decimal.
# Note: This challenge introduces precision problems. The 
# test cases are scaled to six decimal places, though 
# answers with absolute error of up to 10^-4 are acceptable.

# Example
# arr = [1, 1, 0, -1, -1]
# There are n = 5 elements, two positive, two negative 
# and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000,
# and 1/5 = 0.200000. Results are printed as:
# 0.400000
# 0.400000
# 0.200000

# Function Description
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
#     int arr[n]: an array of integers

# Print
# Print the ratios of positive, negative and zero values 
# in the array. Each value should be printed on a separate 
# line with 6 digits after the decimal. The function should 
# not return a value.

# Input Format
# The first line contains an integer, n , the size of the
# array. The second line contains space-separated integers
# that describe arr[n].

# Constraints
#  0 < n <= 100
# -100 <= arr[i] <= 100

# Output Format
# Print the following 3 lines, each to 6 decimals:
#     1. proportion of positive values
#     2. proportion of negative values
#     3. proportion of zeros

# Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
# Sample Output
# 0.500000
# 0.333333
# 0.166667
# Explanation
# There are 3 positive numbers, 2 negative numbers, and 1
# zero in the array. The proportions of occurrence are 
# positive: 3/6 = 0.500000, negative: 2/6 = 0.333333 and 
# zeros: 1/6 = 0.166667. 

