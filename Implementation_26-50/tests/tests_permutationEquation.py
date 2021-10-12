import unittest
import sys
sys.path.append("..")
from implementation import permutationEquation


class test_permutationEquation(unittest.TestCase):
    def testExample(self):
        p = [5, 2, 1, 3, 4]
        self.assertEqual(permutationEquation(p), [4, 2, 5, 1, 3])

    def testZero(self):
        p = [2, 3, 1]
        self.assertEqual(permutationEquation(p), [2, 3, 1])

    def testOne(self):
        p = [4, 3, 5, 1, 2]
        self.assertEqual(permutationEquation(p), [1, 3, 5, 4, 2])


if __name__ == '__main__':
    unittest.main()       



# #26 Sequence Equation
# https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given a sequence of n integers, p[1]...p[n] where 
# each element is distinct and satisfies
#        1 <= p[x] <= n
# For each x where 1 <= x <= n, that is x increments 
# from 1 to n, find any integer y such that 
#       p(p(y)) = x
# and keep a history of the values of y in a return 
# array.

# Example
#  p = [5, 2, 1, 3, 4]
# Each value of x between 1 and 5, the length of the 
# sequence, is analyzed as follows:
#    x = 1 === p[3], p[4] = 3 so p(p[4]) = 1
#    x = 2 === p[2], p[2] = 2 so p(p[2]) = 2
#    x = 3 === p[4], p[5] = 4 so p(p[5]) = 3
#    x = 4 === p[5], p[1] = 5 so p(p[1]) = 4
#    x = 5 === p[1], p[3] = 1 so p(p[3]) = 5
# The values for are [4, 2, 5, 1, 3].

# Function Description
# Complete the permutationEquation function in the editor below.
# permutationEquation has the following parameter(s):
#     int p[n]: an array of integers

# Returns
#     int[n]: the values of y for all x in the 
#             arithmetic sequence to 1 to n

# Input Format
# The first line contains an integer n, the number of
#   elements in the sequence.
# The second line contains n space-separated integers
#   p[i] where 1 <= i <= n.

# Constraints
#   1 <= n <= 50
#   1 <= p[i] <= 50, where 1 <= i <= n.
#   Each element in the sequence is distinct.

# Sample Input 0
# 3
# 2 3 1
# Sample Output 0
# 2
# 3
# 1
# Explanation 0
# Given the values of p(1) = 2, p(2) = 3, and p(3) = 1,
# we calculate and print the following values for each
# x from to 1 to n :
#   x = 1 === p(3) = p(p(2)) = p(p(y)), so we print 
#       the value of y = 2 on a new line.
#   x = 2 === p(1) = p(p(3)) = p(p(y)), so we print 
#       the value of y = 3 on a new line.
#   x = 3 === p(2) = p(p(1)) = p(p(y)), so we print 
#       the value of y = 1 on a new line.

# Sample Input 1
# 5
# 4 3 5 1 2
# Sample Output 1
# 1
# 3
# 5
# 4
# 2