# import math
# import os
# import random
# import re
# import sys



# #create and initialize a list
# list1 = [1,2,3,4,5,6]


# #initialize the middle index with the length of first half
# middle_index=len(list1)//2

# #Split the list from starting index upto middle index in first half
# first_half=list1[:middle_index]

# #Split the list from middle index index upto the last index in second half
# sec_half=list1[middle_index:]

# #printing original lists and two halves
# print('The original list is: ',list1)
# print("First half of list is ",first_half)

# print("Second half of list is ",sec_half)

# a1 = "i"
# a2 = "b"
# a3 = "c"
# # print(a1+a2+a3)

# h = [a1, a2, a3, "p", "l", "q"]
# k = ["0","9","8","7"]
# n = (len(h)//2)
# # m = (len(k)//2)
# # b = (h[0:n])
# # b = "".join(k[:n])

# b = int("".join(k[:n]))
# # j = sum(k[:m])
# print(b)


# text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# # join elements of text with space
# print(' '.join(text))

# # Output: Python is a fun programming language



# def check(i):
#     sq = str(i**2)
#     le = len(str(i))
#     r = sq[-le:]
#     l = sq[:-le] or '0'
#     return sum(map(int,(l,r)))==i

# def kaprekarNumbers(p, q):
#     return [i for i in range(p,q+1) if check(i)]

# p = int(input())
# q = int(input())
# print(*kaprekarNumbers(p, q) or ["INVALID RANGE"])



# def kaprekar(n):
#     d = len(str(n))
#     n_sqr = str(n*n)
#     right = int(n_sqr[len(n_sqr)-d:])
#     left = n_sqr[:len(n_sqr)-d]
#     if left == '':
#         left = 0
#     left = int(left)
#     #print("left:", left, "right:", right)
#     return left+right == n
    
# p = int(input())
# q = int(input())
# a = []
# for i in range(p, q+1):
#     if kaprekar(i):
#         a.append(i)
# if len(a) == 0:
#     print("INVALID RANGE")
# else:
#     print(' '.join(str(c) for c in a))





# lines_yesterday = "50"
# lines_today = "108"
# lines_more = int(lines_today) - int(lines_yesterday)
# print(lines_more)





# workbook = [[[] for i in range(problems_per_page)] for i in range(num_chapters)]
