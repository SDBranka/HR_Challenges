import math
import os
import random
import re
import sys



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
        answ = ""
        for i in range(move_ind+1):
            # clear letters from srt_w
            srt_w.pop(srt_w.index(list_w[i]))
            answ += list_w[i]
        for i in range(len(srt_w)):
            answ += srt_w[i]
    return answ







def biggerIsGreater(w):     #"abdc"
    n = len(w)
    srt_w = sorted(w)       #["a", "b", "c", "d"]
    lst_w = list(w)         #["a", "b", "d", "c"]
    # print(srt_w)
    ind_arr = []
    for i in range(n):
        ind_arr.append(srt_w.index(lst_w[i]))
    print(ind_arr)          #[0, 1, 3, 2]
    zero_ind = ind_arr.index(0)
    for i in range(zero_ind, n - 1):
        # if ind_arr[i] < ind_arr[i-1] and
        pass

        



# Sample Input 1D -- adbc
# srt_w = abcd
# w = "abdc"
# Sample Output 1
# acbd

# Sample Input 0E -- kdhc
# w = "dkhc"
# Sample Output 0
# hcdk


# Sample Input 0A
# w = "ab"
# Sample Output 0
# ba

# Sample Input 0B
# w = "bb"
# Sample Output 0
# no answer

# Sample Input 0C
# w = "hefg"
# Sample Output 0
# hegf

# Sample Input 0D
# w = "dhck"
# Sample Output 0
# dhkc

# Sample Input 4A
# w = "lmno"
# Sample Output 
# lmon

# Sample Input 4B
# w = "dcba"
# Sample Output 
# no answer

# Sample Input 4C
# w = "dcbb"
# Sample Output 
# no answer

# Sample Input 4E
# w = "abcd"
# Sample Output 
# abdc

# Sample Input 4F
w = "fedcbabcd"
# Sample Output 
# fedcbabdc


print(biggerIsGreater1(w))