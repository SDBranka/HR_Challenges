import io
import unittest
import unittest.mock
import sys
sys.path.append("../..")
from warmup_challenges import miniMaxSum0, miniMaxSum1


class test_miniMaxSum0(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        miniMaxSum0(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 2, 3, 4, 5]
        self.assert_stdout(arr, "10 14")


class test_miniMaxSum1(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        miniMaxSum1(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 2, 3, 4, 5]
        self.assert_stdout(arr, "10 14")



if __name__ == '__main__':
    unittest.main()       



# #8 Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given five positive integers, find the minimum and maximum
#  values that can be calculated by summing exactly four of 
# the five integers. Then print the respective minimum and 
# maximum values as a single line of two space-separated 
# long integers.

# Example
# arr = [1, 3, 5, 7, 9]
# The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum
#  is 3 + 5 + 7 + 9 = 24. The function prints
# 16 24

# Function Description
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
#     arr: an array of 5 integers

# Print
# Print two space-separated integers on one line: the 
# minimum sum and the maximum sum of 4 of 5 elements.

# Input Format
# A single line of five space-separated integers.

# Constraints
# 1 <= arr[i] <= 10^9

# Output Format
# Print two space-separated long integers denoting the 
# respective minimum and maximum values that can be 
# calculated by summing exactly four of the five integers. 
# (The output can be greater than a 32 bit integer.)

# Sample Input
# 1 2 3 4 5
# Sample Output
# 10 14
# Explanation
# The numbers are 1, 2, 3, 4, and 5. Calculate the 
# following sums using four of the five integers:
#     Sum everything except 1, the sum is 2 + 3 + 4 + 5 = 14.


# Hints: Beware of integer overflow! Use 64-bit Integer.
# Need help to get started? Try the Solve Me First problem
