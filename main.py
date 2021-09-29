import math
import os
import random
import re
import sys


# ####Implementation#######

# #4 Between Two Sets
# https://www.hackerrank.com/challenges/between-two-sets/problem?h_r=next-challenge&h_v=zen
# There will be two arrays of integers. Determine all 
# integers that satisfy the following two conditions:
#     1. The elements of the first array are all factors 
#       of the integer being considered
#     2. The integer being considered is a factor of all 
#       elements of the second array
# These numbers are referred to as being between the two
# arrays. Determine how many such numbers exist.

# # Example
# a = [2, 6]
# b = [24, 36]
# # There are two numbers between the arrays: 6 and 12.
# # 6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the
# # first value. 12 % 2 = 0, 12 % 6 = 0  and 24 % 12 = 0,
# # 36 % 12 = 0 for the second value. Return 2.

# Function Description
# Complete the getTotalX function in the editor below. 
# It should return the number of integers that are 
# betwen the sets.
# getTotalX has the following parameter(s):
#     int a[n]: an array of integers
#     int b[m]: an array of integers

# Returns
#     int: the number of integers that are between the sets

# Input Format
# The first line contains two space-separated integers,
#   n and m, the number of elements in arrays a and b.
# The second line contains n distinct space-separated 
#   integers a[i] where 0 <= i < n.
# The third line contains m distinct space-separated 
#   integers b[j] where 0 <= j < m.

# Constraints
#  1 <= n,m <= 10
#  1 <= a[i] <= 100
#  1 <= b[j] <= 100

# Sample Input
# 2 3
# 2 4
# 16 32 96
# Sample Output
# 3
# Explanation
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 4, 8 and 16 are the only three numbers for which 
#    each element of a is a factor and each is a factor
#    of all elements of b. 



# def getTotalX(a, b):



# Example
# a = [2, 6]
# b = [24, 36]
# There are two numbers between the arrays: 6 and 12.
# 6 % 2 = 0, 6 % 6 = 0, 24 % 6 = 0 and 36 % 6 = 0 for the
# first value. 12 % 2 = 0, 12 % 6 = 0  and 24 % 12 = 0,
# 36 % 12 = 0 for the second value. Return 2.

# tc 0
# a = [2, 4]
# b = [16, 32, 96]
# Sample Output
# 3

# print(getTotalX(a, b))


































# #9 Divisible Sum Pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen
# Given an array of integers and a positive integer k,
# determine the number of (i, j) pairs where i < j and
# a[i] + a[j] is divisible by k.

# Example
# ar = [1, 2, 3, 4, 5, 6]
# k = 5
# Three pairs meet the criteria: [1, 4], [2, 3] and
# [4, 6].

# Function Description
# Complete the divisibleSumPairs function in the 
# editor below.
# divisibleSumPairs has the following parameter(s):
#     int n: the length of array ar
#     int ar[n]: an array of integers
#     int k: the integer divisor

# Returns
# - int: the number of pairs

# Input Format
# The first line contains 2 space-separated integers,
#   n and k. 
# The second line contains n space-separated integers,
#  each a value of ar[i].

# Constraints
#  2 <= n <= 100
#  1 <= k <= 100
#  1 <= ar[i] <= 100

# Sample Input
# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
# Sample Output
#  5
# Explanation
# Here are the 5 valid pairs when k = 3
#  (0, 2) = ar[0] + ar[2] = 1 + 2 = 3
#  (0, 5) = ar[0] + ar[5] = 1 + 2 = 3
#  (1, 3) = ar[1] + ar[3] = 3 + 6 = 9
#  (2, 4) = ar[2] + ar[4] = 2 + 1 = 3
#  (4, 5) = ar[4] + ar[5] = 1 + 2 = 3



def divisibleSumPairs(n, k, ar):
    pairs = 0

    for i in range(n-1):
        for j in range(n):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    pairs +=1
    return pairs


# Example
# n = 6
# k = 5
# ar = [1, 2, 3, 4, 5, 6]
# Output
# 3

# Sample Input
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
# Sample Output
#  5

print(divisibleSumPairs(n, k, ar))