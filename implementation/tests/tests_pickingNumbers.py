import unittest
import sys
sys.path.append("..")
from implementation import pickingNumbers


class test_pickingNumbers(unittest.TestCase):
    def testExample(self):
        a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
        self.assertEqual(pickingNumbers(a), 5)

    def testZero(self):
        a = [4, 6, 5, 3, 3, 1]
        self.assertEqual(pickingNumbers(a), 3)
        
    def testOne(self):
        a = [1, 2, 2, 3, 1, 2]
        self.assertEqual(pickingNumbers(a), 5)

    def testThree(self):
        a = [4, 2, 3, 4, 4, 9, 98, 98, 3, 3,
            3, 4, 2, 98, 1, 98, 98, 1, 1, 4,
            98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 
            98, 9, 9, 2, 9, 4, 2, 2, 9, 98,
            4, 98, 1, 3, 4, 9, 1, 98, 98, 4,
            2, 3, 98, 98, 1, 99, 9, 98, 98, 3,
            98, 98, 4, 98, 2, 98, 4, 2, 1, 1,
            9, 2, 4]
        self.assertEqual(pickingNumbers(a), 22)

    def testFour(self):
        a = [66] * 100
        self.assertEqual(pickingNumbers(a), 100)


if __name__ == '__main__':
    unittest.main()       



# #16 Picking Numbers
# https://www.hackerrank.com/challenges/picking-numbers/problem
# Given an array of integers, find the longest subarray
# where the absolute difference between any two elements 
# is less than or equal to 1.

# Example
#  a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
# There are two subarrays meeting the criterion: [1, 1, 2, 2]
# and [4, 4, 5, 5, 5]. The maximum length subarray has 5 
# elements.

# Function Description
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
#     int a[n]: an array of integers

# Returns
#     int: the length of the longest subarray that meets the criterion

# Input Format
# The first line contains a single integer n, the size of the
#   array a. 
# The second line contains n space-separated integers, each
#   an a[i].

# Constraints
#   2 <= n <= 100
#   0 <= a[i] < 100
# The answer will be >= 2.

# Sample Input 0
# 6
# 4 6 5 3 3 1
# Sample Output 0
# 3
# Explanation 0
# We choose the following multiset of integers from the 
# array: {4, 3, 3}. Each pair in the multiset has an absolute
# difference <= 1 (i.e. |4-3| = 1 and |3 - 3| = 0), so we 
# print the number of chosen integers, 3, as our answer.

# Sample Input 1
# 6
# 1 2 2 3 1 2
# Sample Output 1
# 5
# Explanation 1
# We choose the following multiset of integers from the 
# array: {1, 2, 2, 1, 2}. Each pair in the multiset has an 
# absolute difference <= 1 (i.e.,|1 - 2| = 1 , |1-1| = 0, 
# and |2- 2| = 0), so we print the number of chosen integers,
# 5, as our answer.
