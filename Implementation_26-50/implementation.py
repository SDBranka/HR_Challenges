import math
import os
import random
import re
import sys


# 26
def permutationEquation(p):
    n = len(p)
    y = []
    for i in range(1, n + 1):
        x = p.index(i)
        print(f"x = {x}")
        y.append(p.index(x + 1) + 1)
    return y


# 27
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


# 28
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


# 29
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


# 30
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


# 31
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


#32
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2 > y1:
        fine = 0
    elif y2 == y1:
        if m2 > m1:
            fine = 0
        elif m2 == m1:
            if d2 >= d1:
                fine = 0
            else:
                fine = 15 * (d1 - d2)
        else:
            fine = 500 * (m1 - m2)
    else:
        fine = 10000
    return fine


# 33
def cutTheSticks(arr):
    answer = [len(arr)]
    while len(arr):
        shortest_stick = min(arr)
        # print(f"shortest_stick = {shortest_stick}")
        arr = list(map(lambda x: x - shortest_stick, arr))
        # print(f"arr after lambda = {arr}")
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                arr.pop(i)
        # print(f"arr pop = {arr}")
        answer.append(len(arr))
    
    answer.pop()
    return answer


# 34
def nonDivisibleSubset(k, s):
    arr = [0]*k
    for i in range(len(s)):
        arr[s[i] % k] += 1
    res = min(arr[0], 1)
    for i in range(1, (k//2) + 1):
        if i != k - i:
            res += max(arr[i], arr[k - i])
        else:
            res += min(arr[i], 1)
    return res


# 35
def taumBday(b, w, bc, wc, z):
    if bc <= wc + z:
        b_buy = bc
    else:
        b_buy = wc + z
    if wc <= bc + z:
        w_buy = wc
    else:
        w_buy = bc + z
    return (b_buy * b) + (w_buy * w)


# 36
# I set out by trying to determine the place where the max and min of each color balls exist, but
# couldn't really decide how to proceed with checking and actually swapping the colors from container
# to container, so I set out on my second attempt which satisfied all the presented test cases.
def organizingContainers0(container):
    n = len(container)
    # find the location of the min and max of each color
    min_locs = []
    max_locs = []
    for i in range(n):
        min_x = 0
        min_y = i
        min = container[0][i]
        max_x = 0
        max_y = i
        max = container[0][i]
        for j in range(n):
            if container[j][i] < min:
                min_x = j
                min_y = i
                min = container[j][i]
            if container[j][i] > max:
                max_x = j
                max_y = i
                max = container[j][i]
        min_locs.append([min_x, min_y])
        max_locs.append([max_x, max_y])
        # print(f"min_locs = {min_locs}")
        # print(f"max_locs = {max_locs}")

def organizingContainers(container):
    n = len(container)
    amount_per_container = []
    num_per_color = [0] * n
    for i in range(n):
        # sum each line to see the max each container can hold
        amount_per_container.append(sum(container[i]))
        # sum the columns of our 2d array to get the total number of each color present
        for j in range(n):
            num_per_color[i] += container[j][i] 
    # print(f"amount_per_container = {amount_per_container}")
    # print(f"num_per_color = {num_per_color}")
    for color in num_per_color:
        # check to see if there is a container that can hold the amount of each color present
        if color in amount_per_container:
            # if a container of the correct size exists remove it from the list of options as it 
            # is now occupied
            amount_per_container.pop(amount_per_container.index(color))
        else:
            # if no container exists to contain a color of balls the swapping is impossible
            return "Impossible"
    # if all balls can fit into containers the swap is possible
    return "Possible"

# 37
def encryption(s):
    L = len(s)
    floor_sqrt_L = math.floor(math.sqrt(L))
    ceil_sqrt_L = math.ceil(math.sqrt(L))
    # print(f"fsL = {floor_sqrt_L}")
    # print(f"csL = {ceil_sqrt_L}")

    broken_s = []
    if floor_sqrt_L * ceil_sqrt_L < L:
        floor_sqrt_L += 1

    for i in range(floor_sqrt_L):
        broken_s.append(s[(i * ceil_sqrt_L):(i * ceil_sqrt_L) + ceil_sqrt_L])

    coded_s = ""
    for i in range(ceil_sqrt_L):
        code = ""
        for j in range(floor_sqrt_L):
            if len(broken_s[j]) > i:
                code += broken_s[j][i]
        coded_s += f"{code} "
    return coded_s

# 38
