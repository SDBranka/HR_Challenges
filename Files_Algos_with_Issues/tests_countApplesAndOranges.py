import io
import unittest
import unittest.mock
import sys
sys.path.append("../..")
from implementation import countApplesAndOranges

class test_countApplesAndOranges(unittest.TestCase):

    # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    # def assert_stdout(self, n, expected_output, mock_stdout):
    #     countApplesAndOranges(n)
    #     self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, s, t, a, b, apples, oranges, expected_output, mock_stdout):
        countApplesAndOranges(s, t, a, b, apples, oranges)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testZero(self):
        s = 7 
        t = 11
        a = 5 
        b = 15
        m = 3 
        n = 2
        apples = [-2, 2, 1]
        oranges = [5, -6]
        self.assert_stdout(s, t, a, b, apples, oranges, "1\n1")

    def testOne(self):
        s = 7
        t = 10
        a = 4
        b = 12
        m = 3
        n = 3 
        apples = [2, 3, -4] 
        oranges = [3, -2, -4] 
        self.assert_stdout(s, t, a, b, apples, oranges, "1\n2")



# countApplesAndOranges(s, t, a, b, apples, oranges)



if __name__ == '__main__':
    unittest.main()       



# #2 Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen
# Sam's house has an apple tree and an orange tree that
# yield an abundance of fruit. Using the information 
# given below, determine the number of apples and 
# oranges that land on Sam's house.

# In the diagram below:
#     The red region denotes the house, where s is the 
#       start point, and t is the endpoint. The apple 
#       tree is to the left of the house, and the orange 
#       tree is to its right.
#     Assume the trees are located on a single point, 
#       where the apple tree is at point a, and the 
#       orange tree is at point b.
#     When a fruit falls from its tree, it lands d units
#       of distance from its tree of origin along the 
#       x-axis. *A negative value of d means the fruit 
#       fell d units to the tree's left, and a positive 
#       value of means it falls d units to the tree's 
#       right. *

# diagram
# a      s    t       b
# a = apple tree
# s = start point
# t = endpoint
# b = orange tree

# Given the value of d for apples and oranges, determine
# how many apples and oranges will fall on Sam's house 
# (i.e., in the inclusive range [s, t])?

# For example, Sam's house is between s = 7 and t = 10. 
# The apple tree is located at a = 4 and the orange at 
# b = 12. There are m = 3 apples and n = 3 oranges. 
# Apples are thrown apples = [2, 3, -4] units distance 
# from a, and oranges = [3, -2, -4] units distance. 
# Adding each apple distance to the position of the 
# tree, they land at [4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]. 
# Oranges land at [12 + 3, 12 + -2, 12 + -4] = [15, 10, 8].
# One apple and two oranges land in the inclusive range
# 7-10 so we print
# 1
# 2

# Function Description
# Complete the countApplesAndOranges function in the 
#   editor below. It should print the number of apples 
#   and oranges that land on Sam's house, each on a 
#   separate line.
# countApplesAndOranges has the following parameter(s):
#     s: integer, starting point of Sam's house location.
#     t: integer, ending location of Sam's house location.
#     a: integer, location of the Apple tree.
#     b: integer, location of the Orange tree.
#     apples: integer array, distances at which each apple falls from the tree.
#     oranges: integer array, distances at which each orange falls from the tree.

# Input Format
# The first line contains two space-separated integers 
# denoting the respective values of s and t.
# The second line contains two space-separated integers
# denoting the respective values of a and b.
# The third line contains two space-separated integers 
# denoting the respective values of m and n.
# The fourth line contains space-separated integers 
# denoting the respective distances that each apple 
# falls from point a.
# The fifth line contains space-separated integers 
# denoting the respective distances that each orange 
# falls from point b.

# Constraints
# 1 <= s, t, a, b, m, n <= 10^
# -10^5 <= d <= 10^5
# a < s < t < b

# Output Format
# Print two integers on two different lines:
#     The first integer: the number of apples that fall on Sam's house.
#     The second integer: the number of oranges that fall on Sam's house.

# Sample Input 0
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6
# Sample Output 0
# 1
# 1
# Explanation 0
# The first apple falls at position 5 - 2 = 3.
# The second apple falls at position 5 + 2 = 7.
# The third apple falls at position 5 + 1 = 6.
# The first orange falls at position 15 + 5 = 20.
# The second orange falls at position 15 - 6 = 9.
# Only one fruit (the second apple) falls within the 
#   region between 7 and 11, so we print 1 as our first 
#   line of output.
# Only the second orange falls within the region 
#   between 7 and 11, so we print 1 as our second line 
#   of output. 






