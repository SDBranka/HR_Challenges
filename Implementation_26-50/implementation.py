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
# misses fringe cases
def biggerIsGreater0(w):
    list_w = list(w)
    answ = "no answer"
    for i in range(len(w) - 1, 0, -1):
        if list_w[i] > list_w[i - 1]:
            list_w[i], list_w[i - 1] = list_w[i - 1], list_w[i]
            answ = ""
            for i in range(len(list_w)):
                answ += list_w[i]
            return answ
    return answ

# index error in removing values from srt_w
def biggerIsGreater1(w):
    n = len(w)
    list_w = list(w)
    srt_w = sorted(w)       
    answ = "no answer"
    loop_run = True
    for i in range(n-1, 0, -1):
        if loop_run:
            for j in range(i-1, -1, -1):
                if list_w[i] > list_w[j]:
                    list_w[i], list_w[j] = list_w[j], list_w[i]
                    loop_run = False
                    move_ind = j
                    break
    if not loop_run:
        ind_arr = []
        for i in range(n):
            ind_arr.append(srt_w.index(list_w[i]))
        print(f"ind_arr={ind_arr}")
        print(f"srt_w = {srt_w}")
        answ = ""
        for i in range(move_ind+1):
            # clear letters from srt_w
            srt_w.pop(ind_arr[i]-i)
            # print(f"i = {i}")
            # print(f"ind_arr[i] = {ind_arr[i]}")
            # print(f"srt_w = {srt_w}")
            answ += list_w[i]
        for i in range(len(srt_w)):
            answ += srt_w[i]
    return answ

# works for all test cases in 0 and 4 but all the hidden cases fail
def biggerIsGreater2(w):
    n = len(w)
    list_w = list(w)
    srt_w = sorted(w)       
    answ = "no answer"
    loop_run = True
    for i in range(n-1, 0, -1):
        if loop_run:
            for j in range(i-1, -1, -1):
                if list_w[i] > list_w[j]:
                    list_w[i], list_w[j] = list_w[j], list_w[i]
                    loop_run = False
                    move_ind = j
                    break
    if not loop_run:
        answ = ""
        for i in range(move_ind+1):
            # clear letters from srt_w
            srt_w.pop(srt_w.index(list_w[i]))
            answ += list_w[i]
        for i in range(len(srt_w)):
            answ += srt_w[i]
    return answ

def biggerIsGreater(w):
    lst_w = list(w)
    n = len(lst_w)
    # Find non-increasing suffix
    i = n - 1
    while i > 0 and lst_w[i - 1] >= lst_w[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    # Find successor to pivot
    j = n - 1
    while lst_w[j] <= lst_w[i - 1]:
        j -= 1
    lst_w[i - 1], lst_w[j] = lst_w[j], lst_w[i - 1]
    
    # Reverse suffix
    lst_w[i : ] = lst_w[n - 1 : i - 1 : -1]
    return "".join(lst_w)

# 39
def getTotalX1(a, b):
    factors_of_b = []
    b_fact = []
    works_w_a = []
    omega_factors = []
    
    # find and build array of factors of integers from array b
    for i in range(len(b)):
        for j in range(1,b[i]+1):
            if b[i] % j == 0:
                factors_of_b.append(j)
    # print(f"factors_of_b: {factors_of_b}")

    # build an array of singular instances of factors that work with each element of array factors_of_b
    for i in range (len(factors_of_b)):
        if factors_of_b.count(factors_of_b[i]) == len(b):
            if factors_of_b[i] not in b_fact:
                b_fact.append(factors_of_b[i])
    # print(f"b_fact: {b_fact}")

    # find and build array of factors of which elements of a are factors
    for i in range (len(a)):
        for j in range(len(b_fact)):
            if b_fact[j] % a[i] == 0:
                works_w_a.append(b_fact[j])
    # print(works_w_a)

    # build array of singular instances that meet all conditions
    for i in range (len(works_w_a)):
        if works_w_a.count(works_w_a[i]) == len(a):
            if works_w_a[i] not in omega_factors:
                omega_factors.append(works_w_a[i])
    # print(omega_factors)

    return (len(omega_factors))

def getTotalX(a, b):
    factors_of_b = []
    b_fact = []
    works_w_a = []
    omega_factors = []
    
    # find and build array of factors of integers from array b
    for i in range(len(b)):
        for j in range(1,b[i]+1):
            if b[i] % j == 0:
                factors_of_b.append(j)
    # print(f"factors_of_b: {factors_of_b}")

    # build an array of singular instances of factors that work with each element of array factors_of_b
    # build an array of singular instances of factors
    b_fact = list(set(factors_of_b))
    # print(f"b_fact: {b_fact}")
    # eliminate elements that arent factors of all elements of b
    i = 0
    while i < len(b_fact):
        if factors_of_b.count(b_fact[i]) != len(b):
            b_fact.pop(i)
        else:
            i += 1
    # print(f"b_fact: {b_fact}")
    
    # find and build array of factors of which elements of a are factors
    for i in range (len(a)):
        for j in range(len(b_fact)):
            if b_fact[j] % a[i] == 0:
                works_w_a.append(b_fact[j])
    # # print(f"works_w_a: {works_w_a}")

    # # build array of singular instances that meet all conditions
    omega_factors = list(set(works_w_a))
    # print(f"omega_factors: {omega_factors}")
    # eliminate elements that arent factors of all elements of b
    i = 0
    while i < len(omega_factors):
        if works_w_a.count(omega_factors[i]) != len(a):
            omega_factors.pop(i)
        else:
            i += 1
    # print(f"omega_factors: {omega_factors}")

    return (len(omega_factors))


# 40
def kaprekarNumbers(p, q):
    answer = []
    
    for i in range(p, q + 1):
        # print(f"i: {i}")
        if i < 4:
            if i == 1:
                answer.append(i)
        else:
            i_squared_str = str(i**2)
            a = int(i_squared_str[:len(i_squared_str)//2])
            # print(f"a: {a}")
            b = int(i_squared_str[len(i_squared_str)//2:])
            # print(f"b: {b}")
            if a + b == i:
                answer.append(i)
    # return answer
    if len(answer) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(x) for x in answer))
        # works too
        # print(f"{' '.join(map(str, answer))}")

# 41
# too slow
def beautifulTriplets0(d, arr):
    triplet_count = 0
    for j in range(1, len(arr)):
        for i in range(j, -1, -1):
            if arr[j] - arr[i] == d:
                for k in range(j + 1, len(arr)):
                    if arr[k] - arr[j] == d:
                        triplet_count += 1
    return triplet_count

# def beautifulTriplets(d, arr):
#     a = set(arr)
#     return len([1 for i in arr if i+d in a and i+d*2 in a])





# Sample Input
# n = 7, d = 3
# arr = [1, 2, 4, 5, 7, 8, 10]
# Sample Output
# 3

# Example
arr = [2, 2, 3, 4, 5]
d = 1
# Output
# 3

# test case 8
# n = 10000 
# d = 1
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#         10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
#         20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
#         40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
#         50, 51, 52, 53, 54, 55, 56, 57, 58, 59,{-truncated-}
#         ..., 10000]
#  Output
# 9996



print(beautifulTriplets(d, arr))