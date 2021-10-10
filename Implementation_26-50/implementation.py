import math
import os
import random
import re
import sys


# 1
def permutationEquation(p):
    n = len(p)
    y = []
    for i in range(1, n + 1):
        x = p.index(i)
        print(f"x = {x}")
        y.append(p.index(x + 1) + 1)
    return y


# 2
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = k%n
    while i != 0:
        # print(f"i = {i}")
        # print(f"i%n = {i%n}")
        if c[i] == 1:
            e -= 3
        else:
            e -= 1
        i = (i + k) % n
        # print(f"i = {i}")
        # print(f"i%n = {i%n}")
    # include the last jump made
    if c[i] == 1:
        e -= 3
    else:
        e -= 1
    return e


# 3
def findDigits(n):
    str_n = str(n)
    m = len(str_n)
    count = 0
    for i in range(m):
        if str_n[i] == "0":
            pass
        elif n % int(str_n[i]) == 0:
            count += 1
    return count


# 4
def extraLongFactorials0(n):
    if n == 1:
        return n
    else:
        return n * extraLongFactorials0(n-1)

def extraLongFactorials(n):
    m = n
    total = m
    if m != 1:
        for i in range(m - 1, 0, -1):
            total *= i
    return total


# 5
def appendAndDelete0(s, t, k):
    ans = "Yes"
    if s == t and k >= (2 * len(t)) + 1:
        return ans
    new_s = []
    for i in range(len(t)):
        if i < len(s):
            if t[i] == s[i]:
                new_s.append(s[i])
            else:
                new_s.append("_")
                k -= 1
        else:
            new_s.append("_")
    while i < len(s) - 1:
        k -= 1
        i += 1        
    if k - new_s.count("_") < 0:
        ans = "No"
    return ans

def appendAndDelete1(s, t, k):
    n = len(s)
    m = len(t)
    count = k
    i = 0
    while i < m and s[i] == t[i]:
        i += 1                
        if i == n - 1:
            break
    needs_to_be_appended = n - i
    count -= needs_to_be_appended
    # if s is longer than t
    if n > m:
        count -= n - m
    # to account for appending the needed letters
    count -= needs_to_be_appended

    if count < 0:
        return "No"
    else:
        return "Yes"

def appendAndDelete2(s, t, k):
    n = len(s)
    m = len(t)
    remove = True
    count = k
    i = 0
    while i < m and s[i] == t[i]:
        if i == n - 1:
            remove = False
            break
        i += 1                
    # counts the length of letters that need to be popped and then appended
    needs_to_be_appended = m - i
    if remove:
        count -= needs_to_be_appended
    # if s is longer than t
    if n > m:
        count -= n - m
    count -= needs_to_be_appended
    if count < 0:
        return "No"
    else:
        return "Yes"


def appendAndDelete(s, t, k):
    count = 0
    n = len(s)
    m = len(t)
    while s[:n]!=t[:n]:
        n -= 1
        count += 1
    need_to_append = ((m - n) + count)
    if k < need_to_append:
        ans = "No"
    elif (n + m) <= k:
        ans = "Yes"
    elif 2 * m < k:
        ans = "Yes"
    elif k % 2 == need_to_append % 2:
        ans = "Yes"
    else:
        ans = "No"
    return ans

# 6
# first solution too slow, second solution solves by checking the first sqrt a<= and the last 
# sqrt >=b and counts the number of whole integers instead of checking to see if each integer 
# between a and b is a sqrt
def squares0(a, b):
    count = 0
    # while a <= b:
    for i in range(a, b+1):
        # squr_a = math.sqrt(a)
        if (i**(0.5)) % 1 == 0:
            # print(f"squr_a = {squr_a}")    
            count += 1
    return count

def squares(a, b):
    count = 0
    squr_a = math.ceil(math.sqrt(a))
    squr_b = math.floor(math.sqrt(b))
    for i in range(squr_a, squr_b+1):
        count +=1
    return count

