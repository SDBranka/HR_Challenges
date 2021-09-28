import math
import os
import random
import re
import sys

# #1 Solve Me First
# https://www.hackerrank.com/challenges/solve-me-first/problem
# Complete the function solveMeFirst to compute
#  the sum of two integers.

# Example
# a = 7
# b = 3
# Return
# 10

# Function Description
# Complete the solveMeFirst function in the editor below.
# solveMeFirst has the following parameters:
#     int a: the first value
#     int b: the second value

# Returns
# - int: the sum of a and b

# Constraints
# 1 <= a, b <= 1000

# Sample Input
# a = 2
# b = 3
# Sample Output
# 5

# Explanation
# 2 + 3 = 5. 

def solveMeFirst(a,b):
    return a + b



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

def simpleArraySum(ar):
    return(sum(ar))



#  #3 Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Alice and Bob each created one problem for HackerRank. 
# A reviewer rates the two challenges, awarding points on 
# a scale from 1 to 100 for three categories: problem 
# clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet 
# a = (a[0], a[1], a[2]), and the rating for Bob's challenge
# is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing 
# a[0] with b[0], a[1] with b[1], and a[2] with b[2].
#     If a[i] > b[i], then Alice is awarded 1 point.
#     If a[i] < b[i], then Bob is awarded 1 point.
#     If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
# Given a and b, determine their respective comparison points.

# Example
# a = [1, 2, 3]
# b = [3, 2, 1]
#     For elements *0*, Bob is awarded a point because a[0] .
#     For the equal elements a[1] and b[1], no points are 
#     earned.
#     Finally, for elements 2, a[2] > b[2] so Alice receives 
#     a point.

# The return array is [1, 1] with Alice's score first 
# and Bob's second.

# Function Description
# Complete the function compareTriplets in the editor below.
# compareTriplets has the following parameter(s):
#     int a[3]: Alice's challenge rating
#     int b[3]: Bob's challenge rating

# Return
#     int[2]: Alice's score is in the first position, 
#     and Bob's score is in the second.

# Input Format
# The first line contains 3 space-separated integers, 
# a[0], a[1], and a[2], the respective values in triplet a.
# The second line contains 3 space-separated integers, 
# b[0], b[1], and b[2], the respective values in triplet b.

# Constraints
#     1 ≤ a[i] ≤ 100
#     1 ≤ b[i] ≤ 100

# Sample Input 0
# 5 6 7
# 3 6 10
# Sample Output 0
# 1 1
# Explanation 0
# In this example:
# Now, let's compare each individual score:
# a[0] > b[0], so Alice receives 1 point.
# a[1] = b[1], so nobody receives a point.
# a[2] < b[2], so Bob receives 1 point.
# Alice's comparison score is 1, and Bob's comparison 
# score is 1. Thus, we return the array [1, 1].

# Sample Input 1
# 17 28 30
# 99 16 8
# Sample Output 1
# 2 1
# Explanation 1
# Comparing the 0th elements, so Bob receives a point.
# Comparing the 1st and 2nd elements, 28 > 16 and 30 > 8
# so Alice receives two points.
# The return array is [2, 1]. 


def compareTriplets(a, b):
    score1 = 0
    score2 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            score1 += 1
        elif a[i] < b[i]:
            score2 += 1            
        
    return [score1, score2]



# #4 A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# In this challenge, you are required to calculate and print 
# the sum of the elements in an array, keeping in mind that 
# some of those integers may be quite large.

# Function Description
# Complete the aVeryBigSum function in the editor below.
# It must return the sum of all array elements.
# aVeryBigSum has the following parameter(s):
#     int ar[n]: an array of integers .

# Return
#     long: the sum of all array elements

# Input Format
# The first line of the input consists of an integer n.
# The next line contains n space-separated integers 
# contained in the array.

# Output Format
# Return the integer sum of the elements in the array.

# Constraints
# 1 <= n <= 10
# 0 <= ar[i] <= 10^10

# Sample Input
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Output
# 5000000015
# Note:
# The range of the 32-bit integer is
# (-2^31) to ((2^31)-1) or [-2147483648, 2147483647]
# When we add several integer values, the resulting 
# sum might exceed the above range. You might need to 
# use long int C/C++/Java to store such sums. 

def aVeryBigSum(ar):
    return(sum(ar))



# #5Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given a square matrix, calculate the absolute difference 
# between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal = 1 + 5 + 9 = 15. The right 
# to left diagonal = 3 + 5 + 9 = 17. Their absolute 
# difference is |15 - 17| = 2

# Function description
# Complete the diagonalDifference function in the 
# editor below.
# diagonalDifference takes the following parameter:
#     int arr[n][m]: an array of integers

# Return
#     int: the absolute diagonal difference

# Input Format
# The first line contains a single integer, n, the number 
# of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and 
# consists of n space-separated integers arr[i][j].

# Constraints
#   -100 <= arr[i][j] <= 100

# Output Format
# Return the absolute difference between the sums of 
# the matrix's two diagonals as a single integer.

# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
# 15
# Explanation
# The primary diagonal is:
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4
# The secondary diagonal is:
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15

# Note: |x| is the absolute value of x

def diagonalDifference(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += arr[i][i] - arr[i][n - 1 - i]
        print(total)
    return abs(total)



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

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zeros = 0
    for num in arr:
        if num == 0:
            zeros += 1
        elif num < 0:
            neg += 1
        else:
            pos += 1
    print("{:.6f}".format(pos / n))
    print("{:.6f}".format(neg / n))
    print("{:.6f}".format(zeros /n))



# #7 Staircase
# https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Staircase detail

# This is a staircase of size n = 4:
#    #
#   ##
#  ###
# ####
# Its base and height are both equal to n. It is drawn 
# using # symbols and spaces. The last line is not 
# preceded by any spaces. Write a program that prints a
# staircase of size n.

# Function Description
# Complete the staircase function in the editor below.
# staircase has the following parameter(s):
#     int n: an integer

# Print
# Print a staircase as described above.

# Input Format
# A single integer, n, denoting the size of the staircase.

# Constraints
# 0 < n <= 100

# Output Format
# Print a staircase of size n using # symbols and spaces.
# Note: The last line must have 0 spaces in it.

# Sample Input
# 6 
# Sample Output
#      #
#     ##
#    ###
#   ####
#  #####  
# ######

# Explanation
# The staircase is right-aligned, composed of # symbols
# and spaces, and has a height and width of n = 6.


def staircase(n):
    for i in range(n):
        step = ""
        for j in range(n):
        
            if j < n - 1-i:
                step += " "
            else:
                step += "#"
        print(step)



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

def miniMaxSum0(arr):
    arr_max = max(arr)
    arr_min = min(arr)
    max_sum = 0
    min_sum = 0

    for num in arr:
        if num == arr_max:
            max_sum += num
        elif num == arr_min:
            min_sum += num
        else:
            max_sum += num
            min_sum += num
        
    print(f"{min_sum} {max_sum}")

def miniMaxSum1(arr):
    max_sum = sum(arr) - min(arr)
    min_sum = sum(arr) - max(arr)
        
    print(f"{min_sum} {max_sum}")



# #9 Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# You are in charge of the cake for a child's birthday. You 
# have decided the cake will have one candle for each year of
# their total age. They will only be able to blow out the 
# tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4, 4, 1, 3]
# The maximum height candles are 4 units high. There are 2 of
#  them, so return 2.

# Function Description
# Complete the function birthdayCakeCandles in the editor
# below.
# birthdayCakeCandles has the following parameter(s):
#     int candles[n]: the candle heights

# Returns
#     int: the number of candles that are tallest

# Input Format
# The first line contains a single integer, n, the size 
# of candles[]. The second line contains n space-separated 
# integers, where each integer describes the height of
# candles[].

# Constraints
# 1 <= n <= 10^5
# 1 <= candles[i] <= 10^7

# Sample Input 0
# 4
# 3 2 1 3
# Sample Output 0
# 2
# Explanation 0
# Candle heights are [3, 2, 1, 3]. The tallest candles
# are 3 units, and there are 2 of them. 

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

# #10 Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given a time in 12 hour AM/PM format, convert it to 
# military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 
# 24-hour clock. 12:00:00PM on a 12-hour clock is 
# 12:00:00 on a 24-hour clock.

# Example
# s = "12:01:00PM"
# Return '12:01:00'.
# s = "12:01:00AM"
# Return '00:01:00'.

# Function Description
# Complete the timeConversion function in the editor below. 
# It should return a new string representing the input time 
# in 24 hour format.
# timeConversion has the following parameter(s):
#     string s: a time in 12 hour format

# Returns
#     string: the time in 24 hour format

# Input Format
# A single string s that represents a time in 12-hour 
# clock format (i.e.: or).

# Constraints
#     All input times are valid

# Sample Input 0
# 07:05:45PM
# Sample Output 0
# 19:05:45

def timeConversion(s):
    hour = s[0]+s[1]
    day_half = s[8] + s[9]
    
    if day_half == "AM":
        if hour == "12":
            z_time = "00" + s[2:8]
        else:
            z_time = s[0:8]
    else:        
        if hour == "12":
            z_time = s[0:8]
        else:
            temp_time = int(hour)
            temp_time += 12
            z_time = str(temp_time) + s[2:8]

    return z_time





