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