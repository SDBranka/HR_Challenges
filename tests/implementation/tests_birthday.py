import unittest
import sys
sys.path.append("../..")
from implementation import birthday


class test_birthday(unittest.TestCase):
    def testExample(self):
        s = [2, 2, 1, 3, 2]
        d = 4
        m = 2
        self.assertEqual(birthday(s, d, m), 2)

    def testZero(self):
        s = [1, 2, 1, 3, 2]
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m), 2)

    def testOne(self):
        s = [1, 1, 1, 1, 1, 1]
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m), 0)

    def testTwo(self):
        s = [4]
        d = 4
        m = 1
        self.assertEqual(birthday(s, d, m), 1)

    def testThree(self):
        s = [2, 5, 1, 3, 4, 4, 3,       
            5, 1, 1, 2, 1, 4, 1,        
            3, 3, 4, 2, 1]
        d = 18
        m = 7
        self.assertEqual(birthday(s, d, m), 3)

    def testThree(self):
        s = [2, 2]
        d = 4
        m = 8
        self.assertEqual(birthday(s, d, m), 1)



if __name__ == '__main__':
    unittest.main()       



# #7 Subarray Division
# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen
# Two children, Lily and Ron, want to share a chocolate
# bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar
# selected such that:
#     The length of the segment matches Ron's birth 
#       month, and,
#     The sum of the integers on the squares is equal
#       to his birth day.
# Determine how many ways she can divide the chocolate.

# Example
# s = [2, 2, 1, 3, 2]
# d = 4
# m = 2
# Lily wants to find segments summing to Ron's birth 
# day, d = 4 with a length equalling his birth month,
# m = 2. In this case, there are two segments meeting
# her criteria: [2, 2] and [1, 3].

# Function Description
# Complete the birthday function in the editor below.
# birthday has the following parameter(s):
#     int s[n]: the numbers on each of the squares of
#        chocolate
#     int d: Ron's birth day
#     int m: Ron's birth month

# Returns
#     int: the number of ways the bar can be divided

# Input Format
# The first line contains an integer n, the number of
#   squares in the chocolate bar.
# The second line contains n space-separated integers
#   s[i], the numbers on the chocolate squares where 
#   0 <= i <= n.
# The third line contains two space-separated integers,
#   d and m, Ron's birth day and his birth month.

# Constraints
#  1 <= n <= 100
#  1 <= s[i] <= 5 where (0 <= i < n)

# Sample Input 0
# 5
# 1 2 1 3 2
# 3 2
# Sample Output 0
# 2
# Explanation 0
# Lily wants to give Ron m = 2 squares summing 
# to d = 3. The following two segments meet the 
# criteria:
# image

# Sample Input 1
# 6
# 1 1 1 1 1 1
# 3 2
# Sample Output 1
# 0
# Explanation 1
# Lily only wants to give Ron m = 2 consecutive 
# squares of chocolate whose integers sum to d = 3.
# There are no possible pieces satisfying these 
# constraints:
# image
# Thus, we print 0 as our answer.

# Sample Input 2
# 1
# 4
# 4 1
# Sample Output 2
# 1
# Explanation 2
# Lily only wants to give Ron m = 1 square of 
# chocolate with an integer value of d = 4. Because 
# the only square of chocolate in the bar satisfies 
# this constraint, we print 1 as our answer.
