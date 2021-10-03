import math
import os
import random
import re
import sys


# ####Implementation#######

# def formingMagicSquare0(s):
#     n = len(s)
#     # # print(s)
#     # # horizontal sums
#     horz_sums = [sum(line) for line in s]
#     print(horz_sums)
#     # # horz_sums
#     for i, h_sum in enumerate(horz_sums):
#         horz_sums[i] = abs(h_sum - 15)
#     print(horz_sums)

#     # # vertical sums
#     vert_sums = []
#     for col in range(n):
    #     vert_sums.append(sum(row[col] for row in s))
    # # vert_sums = [sum(row[col] for row in s)]
    # print(vert_sums)
    # # # vert_sums
    # for i, v_sum in enumerate(vert_sums):
    #     vert_sums[i] = abs(v_sum - 15)
    # print(vert_sums)

    # # diags
    # diag_sums = []
    # # # diag downright sum
    # dr = 0
    # for i in range(n):
    #     dr +=s[i][i]
    # diag_sums.append(dr)  

    # # diag upright sum
    # ur = 0
    # for i in range(n-1,-1,-1):
    #     ur +=s[i][i]
    # diag_sums.append(ur)  

    # # # diag_sums
    # for i, d_sum in enumerate(diag_sums):
    #     diag_sums[i] = abs(d_sum - 15)
    # # # print(diag_sums)

    # all_sums = [horz_sums, vert_sums, diag_sums ]
    # print(all_sums)

    # # safe_pos = []
    # # # solve the diagonals
    # # # dr
    # # if diag_sums[0] == 0:
    # #     safe_pos.append([[0, 0], [1, 1], [2, 2]])
    # # elif diag_sums[1] == 0:
    # #     safe_pos.append([[2, 0], [1, 1], [2, 0]])

    # prob_pos = []
    # # solve the diagonals
    # # dr
    # if diag_sums[0] == 0:
    #     prob_pos.append([[0, 0], [1, 1], [2, 2]])
    # elif diag_sums[1] == 0:
    #     prob_pos.append([[2, 0], [1, 1], [2, 0]])


    

    













def formingMagicSquare(s):
    valid_combs = [[9, 5, 1], [9, 1, 5], [5, 9, 1], [5, 1, 9], [1, 9, 5], [1, 5, 9],
                    [7, 5, 3], [7, 3, 5], [3, 5, 7], [3, 7, 5], [5, 3, 7], [5, 7, 3],
                    [2, 5, 8], [2, 8, 5], [8, 2, 5], [8, 5, 2], [5, 2, 8], [5, 8, 2], 
                    [4, 5, 6], [4, 6, 5], [6, 5, 4], [6, 4, 5], [5, 6, 4], [5, 4, 6],
                    [2, 9, 4], [2, 4, 9], [9, 4, 2], [9, 2, 4], [4, 9, 2], [4, 2, 9], 
                    [6, 1, 8], [6, 8, 1], [1, 6, 8], [1, 8, 6], [8, 6, 1], [8, 1, 6], 
                    [6, 7, 2], [6, 2, 7], [7, 6, 2], [7, 2, 6], [2, 7, 6], [2, 6, 7],
                    [8, 3, 4], [8, 4, 3], [3, 4, 8], [3, 8, 4], [4, 3, 8], [4, 8, 3]
    ]
    avail_pos = [[0, 0], [0, 1], [0, 2],
                [1, 0], [1, 1], [1, 2],
                [2, 0], [2, 1], [2, 2]
    ]
    n = len(s)
    safe_pos = []


    for i, row in enumerate(s):
        # horizontal check
        # print(row)
        if row in valid_combs:
            safe_pos.append([i, 0])
            safe_pos.append([i, 1])
            safe_pos.append([i, 2])
    # print(safe_pos)


    # vertical check
    # build columns
    for c in range(n):
        vert_col = []
        for r in range(n):
            vert_col.append(s[r][c])
        # see is column is valid
        if vert_col in valid_combs:
            safe_pos.append([0, c])
            safe_pos.append([1, c])
            safe_pos.append([2, c])

    # print(safe_pos)
    # print(sorted(safe_pos))

    #Diagonals Part
    dr = [s[0][0], s[1][1], s[2][2]]
    # print(dr)
    if dr in valid_combs:
        safe_pos.append([0, 0])
        safe_pos.append([1, 1])
        safe_pos.append([2, 2])
    
    ur = [s[2][0], s[1][1], s[0][2]]
    # print(ur)
    if ur in valid_combs:
        safe_pos.append([0, 2])
        safe_pos.append([1, 1])
        safe_pos.append([2, 0])
    # print(f"safe_pos ur = {safe_pos}")

    # find spaces that require change
    prob_pos = []
    for pos in avail_pos:
        if pos not in safe_pos:
            prob_pos.append(pos)

    # print(prob_pos)






s = [[5, 3, 4], 
    [1, 5, 8], 
    [6, 4, 2]
    ]





# Example
# s = [[5, 3, 4], 
#     [1, 5, 8], 
#     [6, 4, 2]
#     ]
# The matrix looks like this:
# 5 3 4
# 1 5 8
# 6 4 2
# We can convert it to the following magic square:
# 8 3 4
# 1 5 9
# 6 7 2
# This took three replacements at a cost of
# |5 - 8| + |8 - 9| +|4 - 7| = 7


# Sample Input 0
# s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
# Sample Output 0
# 1
# Explanation 0
# If we change the bottom right value, s[2][2], from 5 to 6 at
# a cost of |6 - 5| = 1, s becomes a magic square at the 
# minimum possible cost.

# Sample Input 1
# s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
# Sample Output 1
# 4
# Explanation 1
# Using 0-based indexing, if we make
# s[0][1] -> 9 at a cost of |9 - 8| = 1
# s[1][0] -> 3 at a cost of |3 - 4| = 1
# s[2][0] -> 8 at a cost of |8 - 6| = 2,
# then the total cost will be 1 + 1 + 2 = 4. 


formingMagicSquare(s)