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



# #2 Simple Array Sum
# https://www.hackerrank.com/challenges/simple-array-sum/problem?h_r=next-challenge&h_v=zen
# Given an array of integers, find the sum of its elements.

# For example, if the array ar = [1, 2, 3], 1 + 2 + 3 = 6, 
# so return 6

# Function Description
# Complete the simpleArraySum function in the editor 
# below. It must return the sum of the array elements as 
# an integer.

# simpleArraySum has the following parameter(s):
#     ar: an array of integers

# Input Format
# The first line contains an integer, n, denoting the 
# size of the array. The second line contains n 
# space-separated integers representing the array's elements.

# Constraints
# < n, ar[i] <= 1000

# Output Format
# Print the sum of the array's elements as a single integer.

# Sample Input
# 6
# 1 2 3 4 10 11
# Sample Output
# 31

# Explanation
# We print the sum of the array's elements: 1 + @ + 3 + 4 + 10 + 11 = 31
# .
