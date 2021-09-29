import math
import os
import random
import re
import sys


# #1 Electronics Shop
# https://www.hackerrank.com/challenges/electronics-shop/problem
# A person wants to determine the most expensive computer
# keyboard and USB drive that can be purchased with a 
# give budget. Given price lists for keyboards and USB 
# drives and a budget, find the cost to buy them. If
# it is not possible to buy both items, return -1.

# Example
# b = 60
# keyboards = [40, 50, 60]
# drives = [5, 8, 12]
# The person can buy a 40 keyboar + 12 USB drive = 52,
# or a 50 keyboard + 8 USB drive = 58.
# Choose the latter as the more expensive option and 
# return 58

# Function Description
# Complete the getMoneySpent function in the editor below.
# getMoneySpent has the following parameter(s):
#     -int keyboards[n]: the keyboard prices
#     -int drives[m]: the drive prices
#     -int b: the budget

# Returns
#     -int: the maximum that can be spent, or -1
#           if it is not possible to buy both items

# Input Format
# The first line contains three space-separated integers
# b, n, and m, the budget, the number of keyboard models 
# and the number of USB drive models.
# The second line contains n space-separated integers 
# keyboard[i], the prices of each keyboard model.
# The third line contains mspace-separated integers
# drives, the prices of the USB drives.

# Constraints
#   1 <= m,n <= 1000
#   1 <= b <= 10^6
#   The price of each item is in the inclusive range [1, 10^6]

# Example:
# Input 0
# 10 2 3
# 3 1
# 5 2 8
# Output 0
# 9
# Explanation 0
# Buy the 2nd keyboard and the 3rd USB drive 
# for a total cost of 8 + 1 = 9.

# Example
# Input 1
# 5 1 1
# 4
# 5
# Output 1
# -1
# Explanation 1
# There is no way to buy one keyboard and one USB drive 
# because 4 + 5 > 5, so return -1.

# Complete the getMoneySpent function below.

def getMoneySpent(keyboards, drives, b):
    max_budget = 0
    # comparer the prices of each available pair
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            combined_price = keyboards[i] + drives[j]
            # check if they are in the budget
            if combined_price <= b:
                # check if it is greater than the current max_budet
                if combined_price > max_budget:
                    max_budget = combined_price

    # if no items may be purechase return -1
    if max_budget <= 0:
        return -1
    # else return the maximum that may be spent
    return max_budget



# #2 Equalize the Array
# https://www.hackerrank.com/challenges/equality-in-a-array/problem
# Given an array of integers, determine the minimum number
# of elements to delete to leave only elements of equal value.

# Example
# arr = [1, 2, 2, 3]

# Delete the 2 elements 1 and 3 leaving arr = [2, 2].
# If both twos plus either the 1 or the 3 are deleted, 
# it takes 3 deletions to leave either [3] or [1].
# The minimum number of deletions is 2.

# Function Description
# Complete the equalizeArray function in the editor below.
# equalizeArray has the following parameter(s):
#     int arr[n]: an array of integers

# Returns
#     int: the minimum number of deletions required

# Input Format
# The first line contains an integer n, the number of 
# elements in arr. The next line contains n space-separated 
# integers arr[i].

# Constraints
#   1 <= n <= 100
#   1 <= arr[i] <= 100

# Sample Input
# STDIN       Function
# -----       --------
# 5           arr[] size n = 5
# 3 3 2 1 3   arr = [3, 3, 2, 1, 3]
# Sample Output
# 2   
# Explanation
# Delete arr[2] = 2 and arr[3] = 1 to leave arr' = [3, 3, 3]. 
# This is minimal. The only other options are to delete 4 
# elements to get an array of either [1] or [2].


def equalizeArray(arr):
    min_num_deletions = 0

    # get singular number occurences
    nums_in_arr = []
    nums_in_arr.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            nums_in_arr.append(arr[i+1])

    # find most prevalent number
    highest_count = 0
    most_of_num = nums_in_arr[0]
    for i in range(len(nums_in_arr)):
        count_num = arr.count(nums_in_arr[i])
        # print(count_num)
        if count_num > highest_count:
            most_of_num = nums_in_arr[i]
            highest_count = count_num
    # count the number of deletions
    for i in range(len(arr)):
        if arr[i] != most_of_num:
            min_num_deletions += 1

    return min_num_deletions






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


