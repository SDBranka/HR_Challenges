import unittest
import sys
sys.path.append("..")
from implementation import circularArrayRotation


class test_assertEqualcircularArrayRotation(unittest.TestCase):
    def testExample(self):
        a = [3, 4, 5]
        k = 2
        queries = [1, 2]
        self.assertEqual(circularArrayRotation(a, k, queries), [5, 3])

    def testFifteen(self):
        a = [1, 2, 3]
        k = 2
        queries = [0, 1, 2]
        self.assertEqual(circularArrayRotation(a, k, queries), [2, 3, 1])

    def testZero(self):
        k = 51
        a = [39356, 87674, 16667, 54260, 43958,
            70429, 53682, 6169, 87496, 66190,
            90286, 4912, 44792, 65142, 36183,
            43856, 77633, 38902, 1407, 88185,
            80399, 72940, 97555, 23941, 96271, 
            49288, 27021, 32032, 75662, 69161,
            33581, 15017, 56835, 66599, 69277,
            17144, 37027, 39310, 23312, 24523,
            5499, 13597, 45786, 66642, 95090,
            98320, 26849, 72722, 37221, 28255,
            60906
        ]
        queries = [47, 10, 12, 13, 6,
                29, 22, 17, 7, 3,
                30, 45, 1, 21, 50,
                17, 25, 42, 5, 6,
                47, 2, 24, 1, 6, 
                14, 24, 43, 7, 2, 
                35, 3, 13, 22, 16,
                19, 0, 12, 10, 32,
                41, 14, 1, 42, 35,
                0, 9, 34, 17, 14,
                15, 38, 17, 13, 40,
                48, 27, 38, 41, 8,
                14, 25, 11, 27, 47,
                2, 20, 22, 39, 4,
                28, 29, 43, 29, 21,
                1, 4, 4, 10, 46,
                43, 50, 33, 34, 12,
                47, 32, 13, 8, 47,
                22, 23, 21, 33, 24,
                43, 35, 19, 39, 24
        ]
        self.assertEqual(circularArrayRotation(a, k, queries), [72722, 90286, 44792, 65142, 53682,
                                                                69161, 97555, 38902, 6169, 54260,
                                                                33581, 98320, 87674, 72940, 60906,
                                                                38902, 49288, 45786, 70429, 53682,
                                                                72722, 16667, 96271, 87674, 53682,
                                                                36183, 96271, 66642, 6169, 16667,
                                                                17144, 54260, 65142, 97555, 77633,
                                                                88185, 39356, 44792, 90286, 56835,
                                                                13597, 36183, 87674, 45786, 17144, 
                                                                39356, 66190, 69277, 38902, 36183,
                                                                43856, 23312, 38902, 65142, 5499,
                                                                37221, 32032, 23312, 13597, 87496,
                                                                36183, 49288, 4912, 32032, 72722, 
                                                                16667, 80399, 97555, 24523, 43958,
                                                                75662, 69161, 66642, 69161, 72940,
                                                                87674, 43958, 43958, 90286, 26849,
                                                                66642, 60906, 66599, 69277, 44792,
                                                                72722, 56835, 65142, 87496, 72722,
                                                                97555, 23941, 72940, 66599, 96271,
                                                                66642, 17144, 88185, 24523, 96271
                                                            ])


if __name__ == '__main__':
    unittest.main()    



# #25 Circular Array Rotation
# https://www.hackerrank.com/challenges/circular-array-rotation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# John Watson knows of an operation called a right 
# circular rotation on an array of integers. One 
# rotation operation moves the last array element to
# the first position and shifts all remaining elements
# right one. To test Sherlock's abilities, Watson 
# provides Sherlock with an array of integers. 
# Sherlock is to perform the rotation operation a 
# number of times then determine the value of the 
# element at a given position.
# For each array, perform a number of right circular
# rotations and return the values of the elements at
# the given indices.

# Example
# a = [3, 4, 5]
# k = 2
# queries = [1, 2]
# Here k is the number of rotations on a, and queries 
# holds the list of indices to report. First we 
# perform the two rotations: 
#   [3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]
# Now return the values from the zero-based indices 
# 1 and 2 as indicated in the queries array.
# a[1] = 5
# a[2] = 3

# Function Description
# Complete the circularArrayRotation function in the
#   editor below.
# circularArrayRotation has the following parameter(s):
#     int a[n]: the array to rotate
#     int k: the rotation count
#     int queries[1]: the indices to report

# Returns
#     int[q]: the values in the rotated a as requested
#        in m

# Input Format
# The first line contains 3 space-separated integers,
#       n, k, and q, the number of elements in the 
#       integer array, the rotation count and the 
#       number of queries.
# The second line contains n space-separated integers,
#       where each integer i describes array element 
#       a[i] (where 0 <= i <= n).
# Each of the subsequent q lines contains a single 
#       integer, queries[i], an index of an element 
#       in a to return.

# Constraints
#   1 <= n <= 10^5
#   1 <= a[i] <= 10^5
#   1 <= k <= 10^5
#   1 <= q <= 500
#   0 <= queries[i] < n

# Sample Input 0
# 3 2 3
# 1 2 3
# 0
# 1
# 2
# Sample Output 0
# 2
# 3
# 1
# Explanation 0
# After the first rotation, the array is [3, 1, 2].
# After the second (and final) rotation, the array
#   is [2, 3, 1].
# We will call this final state array b = [2, 3, 1].
#   For each query, we just have to get the value of
#   b(queries[i]).
# queries[0] = 0, b[0] = 2,
# queries[1] = 1, b[1] = 3,
# queries[2] = 2, b[2] = 1 

