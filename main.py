import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = k%n
    while i != 0:
        print(f"i = {i}")
        print(f"i%n = {i%n}")

        if c[i] == 1:
            e -= 3
        else:
            e -= 1
        i = (i + k) % n
        print(f"i = {i}")
        print(f"i%n = {i%n}")

    # include the last jump made
    if c[i] == 1:
        e -= 3
    else:
        e -= 1
    return e


# Example.
# c = [0, 0, 1, 0]
# k = 2
# Output
# 96.

# Sample Input
# k = 2
# c = [0, 0, 1, 0, 0, 1, 1, 0]
# Sample Output
# 92

# Sample Input 2
k = 19
c = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
# Sample Output
# 97


print(jumpingOnClouds(c, k))