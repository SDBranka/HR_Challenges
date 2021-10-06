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

