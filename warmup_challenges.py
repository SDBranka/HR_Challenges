import math
import os
import random
import re
import sys


def solveMeFirst(a,b):
    return a + b


def simpleArraySum(ar):
    return(sum(ar))


def compareTriplets(a, b):
    score1 = 0
    score2 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            score1 += 1
        elif a[i] < b[i]:
            score2 += 1            
        
    return [score1, score2]


def aVeryBigSum(ar):
    return(sum(ar))


def diagonalDifference(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += arr[i][i] - arr[i][n - 1 - i]
        print(total)
    return abs(total)


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


def staircase(n):
    for i in range(n):
        step = ""
        for j in range(n):
        
            if j < n - 1-i:
                step += " "
            else:
                step += "#"
        print(step)


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


def birthdayCakeCandles(candles):
    return candles.count(max(candles))


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


