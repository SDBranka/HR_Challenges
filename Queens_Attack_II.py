import math
import os
import random
import re
import sys



# #3 Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
# You will be given a square chess board with one queen and 
# a number of obstacles placed on it. Determine how many 
# squares the queen can attack.

# A queen is standing on an n * n chessboard. The chess 
# board's rows are numbered from 1 to n, going from bottom 
# to top. Its columns are numbered from 1 to n, going from 
# left to right. Each square is referenced by a tuple, (r, c),
# describing the row, r, and column, c, where the square is 
# located.

# The queen is standing at position (rq, cq). In a single 
# move, she can attack any square in any of the eight 
# directions (left, right, up, down, and the four diagonals). 
# In the diagram below, the green circles denote all the 
# cells the queen can attack from (4, 4):

# image

# There are obstacles on the chessboard, each preventing 
# the queen from attacking any square beyond it on that 
# path. For example, an obstacle at location (3, 5) in the 
# diagram above prevents the queen from attacking cells (3, 5),
# (2, 6), and (1, 7):

# image

# Given the queen's position and the locations of all the 
# obstacles, find and print the number of squares the queen 
# can attack from her position at (rq, cq). In the board 
# above, there are 24 such squares.

# Function Description
# Complete the queensAttack function in the editor below.
# queensAttack has the following parameters:
# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of 2
#   integers, the row and column of an obstacle

# Returns
# - int: the number of squares the queen can attack

# Input Format
# The first line contains two space-separated integers n
# and k, the length of the board's sides and the number 
# of obstacles. The next line contains two space-separated
# integers rq and cq, the queen's row and column position.
# Each of the next lines k contains two space-separated 
# integers r[i] and c[i] , the row and column position of
# obstacle[i].

# Constraints
#   0 < n <= 10^5
#   0 <= k <= 10^5
#     A single cell may contain more than one obstacle.
#     There will never be an obstacle at the position where the queen is located.

# Subtasks

# For 30% of the maximum score:
        # 0 < n <= 100
        # 0 <= k <= 100
# For 55% of the maximum score:
        # 0 < n <= 1000
        # 0 <= k <= 10^5



# Sample Input 0
# 4 0
# 4 4
# Sample Output 0
# 9

# Explanation 0
# The queen is standing at position (4, 4) on a $x4 
# chessboard with no obstacles:

# image

# Sample Input 1
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
# Sample Output 1
# 10

# Explanation 1
# The queen is standing at position (4, 3) on a 5x5 
# chessboard with k = 3 obstacles:

# image

# The number of squares she can attack from that position 
# is 10.

# Sample Input 2
# 1 0
# 1 1
# Sample Output 2
# 0

# Explanation 2
# Since there is only one square, and the queen is on it,
#  the queen can move 0 squares.


def queensAttack0(n, k, r_q, c_q, obstacles):
    pos_to_attack = 0
    # build map
    map = []
    for i in range(n):
        map_row = []
        for j in range(n):
            if [i + 1, j + 1] in obstacles:
                map_symbol = "X"
            elif [i + 1, j + 1] == [r_q, c_q]:
                map_symbol = "Q"
            else:
                map_symbol = "_"
            map_row.append(map_symbol)
        map.append(map_row)
    # print(map)

    # another way to build the map
    # for row in range(n):
    #     r = ["_"] * n
    #     map.append(r)

    # # place queen
    # map[r_q-1][c_q-1] = "Q"
    # # offset by one to convert to array index address
    queen_pos_r = r_q - 1
    queen_pos_c = c_q - 1
    # # print(map)

    # # place obstacles
    # for i in range(len(obstacles)):
    #     map[obstacles[i][0]-1][obstacles[i][1]-1] = "X"
    # # print(map)

    # check in direction
    # left
    check_dir = queen_pos_c - 1
    if check_dir >= 0:
        while check_dir >= 0:
            # print(f"check_dir left = {check_dir}")
            if map[queen_pos_r][check_dir] in obstacles:
                # print("X left")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck left = {pos_to_attack}")
            check_dir -= 1
    # right
    check_dir = queen_pos_c + 1
    if check_dir < n:
        while check_dir < n:
            # print(f"check_dir right = {check_dir}")
            if map[queen_pos_r][check_dir] in obstacles:
                # print("X right")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck right = {pos_to_attack}")
            check_dir += 1

    # check in y direction
    # down
    check_dir = queen_pos_r + 1
    if check_dir < n:
        while check_dir < n:
            # print(f"check_dir down = {check_dir}")
            if map[check_dir][queen_pos_c] in obstacles:
                # print("X down")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck down = {pos_to_attack}")
            check_dir += 1

    # up
    check_dir = queen_pos_r - 1
    if check_dir >= 0:
        while check_dir >= 0:
            # print(f"check_dir up = {check_dir}")
            if map[queen_pos_r][check_dir] in obstacles:
                # print("X up")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck up = {pos_to_attack}")
            check_dir -= 1


    # check diags
    # downleft
    check_dir_r = queen_pos_r + 1
    check_dir_c = queen_pos_c - 1
    if check_dir_r < n and check_dir_c >= 0:
        while check_dir_r < n and check_dir_c >= 0:
            # print(f"check_dir_r dl = {check_dir_r}")
            # print(f"check_dir_c dl =  {check_dir_c}")
            if map[check_dir_r][check_dir_c] in obstacles:
                # print("X dl")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck dl = {pos_to_attack}")
            check_dir_r += 1
            check_dir_c -= 1

    # downright
    check_dir_r = queen_pos_r + 1
    check_dir_c = queen_pos_c + 1
    if check_dir_r < n and check_dir_c < n:
        while check_dir_r < n and check_dir_c < n:
            # print(f"check_dir_r dr = {check_dir_r}")
            # print(f"check_dir_c dr =  {check_dir_c}")
            if map[check_dir_r][check_dir_c] in obstacles:
                # print("X dr")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck dr = {pos_to_attack}")
            check_dir_r += 1
            check_dir_c += 1

    # upleft
    check_dir_r = queen_pos_r - 1
    check_dir_c = queen_pos_c - 1
    if check_dir_r >= 0 and check_dir_c >= 0:
        while check_dir_r >= 0 and check_dir_c >= 0:
            # print(f"check_dir_r ul = {check_dir_r}")
            # print(f"check_dir_c ul =  {check_dir_c}")
            if map[check_dir_r][check_dir_c] in obstacles:
                # print("X ul")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck ul = {pos_to_attack}")
            check_dir_r -= 1
            check_dir_c -= 1

    # upright
    check_dir_r = queen_pos_r - 1
    check_dir_c = queen_pos_c + 1
    if check_dir_r >= 0 and check_dir_c < n:
        while check_dir_r >= 0 and check_dir_c < n:
            # print(f"check_dir_r ur = {check_dir_r}")
            # print(f"check_dir_c ur =  {check_dir_c}")
            if map[check_dir_r][check_dir_c] in obstacles:
                # print("X ur")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck ur = {pos_to_attack}")
            check_dir_r -= 1
            check_dir_c += 1
    return pos_to_attack


# 
# 
# 
# 

def queensAttack(n, k, r_q, c_q, obstacles):
    pos_to_attack = 0
    queen_pos_r = r_q - 1
    queen_pos_c = c_q - 1


    # check in direction
    # left
    check_dir = queen_pos_c - 1
    if check_dir >= 0:
        while check_dir >= 0:
            print(f"check_dir left = {check_dir}")
            # print(f"queen_pos_r = {queen_pos_r}")

            # adjust these values by one to acconnodate index 
            # shift for obstacles coordinates
            if [queen_pos_r + 1, check_dir + 1] in obstacles:
                print("X left")
                break
            else:
                pos_to_attack += 1
                print(f"pos_to_attck left = {pos_to_attack}")
            check_dir -= 1
    # right
    check_dir = queen_pos_c + 1
    if check_dir < n:
        while check_dir < n:
            # print(f"check_dir right = {check_dir}")
            if [queen_pos_r + 1, check_dir + 1] in obstacles:
                # print("X right")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck right = {pos_to_attack}")
            check_dir += 1
    # down
    check_dir = queen_pos_r + 1
    if check_dir < n:
        while check_dir < n:
            # print(f"check_dir down = {check_dir}")
            if [check_dir + 1, queen_pos_c + 1] in obstacles:
                # print("X down")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck down = {pos_to_attack}")
            check_dir += 1
    # up
    check_dir = queen_pos_r - 1
    if check_dir >= 0:
        while check_dir >= 0:
            # print(f"check_dir up = {check_dir}")
            if [queen_pos_r + 1, check_dir + 1] in obstacles:
                # print("X up")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck up = {pos_to_attack}")
            check_dir -= 1
    # downleft
    check_dir_r = queen_pos_r + 1
    check_dir_c = queen_pos_c - 1
    if check_dir_r < n and check_dir_c >= 0:
        while check_dir_r < n and check_dir_c >= 0:
            # print(f"check_dir_r dl = {check_dir_r}")
            # print(f"check_dir_c dl =  {check_dir_c}")
            if [check_dir_r + 1, check_dir_c + 1] in obstacles:
                # print("X dl")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck dl = {pos_to_attack}")
            check_dir_r += 1
            check_dir_c -= 1
    # downright
    check_dir_r = queen_pos_r + 1
    check_dir_c = queen_pos_c + 1
    if check_dir_r < n and check_dir_c < n:
        while check_dir_r < n and check_dir_c < n:
            # print(f"check_dir_r dr = {check_dir_r}")
            # print(f"check_dir_c dr =  {check_dir_c}")
            if [check_dir_r + 1, check_dir_c + 1] in obstacles:
                # print("X dr")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck dr = {pos_to_attack}")
            check_dir_r += 1
            check_dir_c += 1
    # upleft
    check_dir_r = queen_pos_r - 1
    check_dir_c = queen_pos_c - 1
    if check_dir_r >= 0 and check_dir_c >= 0:
        while check_dir_r >= 0 and check_dir_c >= 0:
            # print(f"check_dir_r ul = {check_dir_r}")
            # print(f"check_dir_c ul =  {check_dir_c}")
            if [check_dir_r + 1, check_dir_c + 1] in obstacles:
                # print("X ul")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck ul = {pos_to_attack}")
            check_dir_r -= 1
            check_dir_c -= 1
    # upright
    check_dir_r = queen_pos_r - 1
    check_dir_c = queen_pos_c + 1
    if check_dir_r >= 0 and check_dir_c < n:
        while check_dir_r >= 0 and check_dir_c < n:
            # print(f"check_dir_r ur = {check_dir_r}")
            # print(f"check_dir_c ur =  {check_dir_c}")
            if [check_dir_r + 1, check_dir_c + 1] in obstacles:
                # print("X ur")
                break
            else:
                pos_to_attack += 1
                # print(f"pos_to_attck ur = {pos_to_attack}")
            check_dir_r -= 1
            check_dir_c += 1

    return pos_to_attack



n = 10
k = 10
r_q = 5
c_q = 8
obstacles = [[2, 3],
            [3, 7],
            [4, 8],
            [4, 9],
            [5, 2],
            [5, 9],
            [6, 7],
            [6, 9],
            [7, 4],
            [10, 10],
]
#   0 1 2 3 4 5 6 7 8 9
# 0 - - - - - - - - - -
# 1 - - x - - - - - - -
# 2 - - - - - - x - - -
# 3 - - - - - - - x x -
# 4 - - x - - - - Q x -
# 5 - - - - - - x - x - 
# 6 - - - x - - - - - - 
# 7 - - - - - - - - - - 
# 8 - - - - - - - - - - 
# 9 - - - - - - - - - x


# 4 + 0 + 5 + 0 + 0 + 0 + 0 + 4
    # def testFive(self):
# n = 100
# k = 100
# r_q = 48
# c_q = 81
# obstacles = [[54, 87],
#             [64, 97],
#             [42, 75],
#             [32, 65],
#             [42, 87],
#             [32, 97],
#             [54, 75],
#             [64, 65],
#             [48, 87],
#             [48, 75],
#             [54, 81],
#             [42, 81],
#             [45, 17],
#             [14, 24],
#             [35, 15],
#             [95, 64],
#             [63, 87],
#             [25, 72],
#             [71, 38],
#             [96, 97],
#             [16, 30],
#             [60, 34],
#             [31, 67],
#             [26, 82],
#             [20, 93],
#             [81, 38],
#             [51, 94],
#             [75, 41],
#             [79, 84],
#             [79, 65],
#             [76, 80],
#             [52, 87],
#             [81, 54],
#             [89, 52],
#             [20, 31],
#             [10, 41],
#             [32, 73],
#             [83, 98],
#             [87, 61],
#             [82, 52],
#             [80, 64],
#             [82, 46],
#             [49, 21],
#             [73, 86],
#             [37, 70],
#             [43, 12],
#             [94, 28],
#             [10, 93],
#             [52, 25],
#             [50, 61],
#             [52, 68],
#             [52, 23],
#             [60, 91],
#             [79, 17],
#             [93, 82],
#             [12, 18],
#             [75, 64],
#             [69, 69],
#             [94, 74],
#             [61, 61],
#             [46, 57],
#             [67, 45],
#             [96, 64],
#             [83, 89],
#             [58, 87],
#             [76, 53],
#             [79, 21],
#             [94, 70],
#             [16, 10],
#             [50, 82],
#             [92, 20],
#             [40, 51],
#             [49, 28],
#             [51, 82],
#             [35, 16],
#             [15, 86],
#             [78, 89],
#             [41, 98],
#             [70, 46],
#             [79, 79],
#             [24, 40],
#             [91, 13],
#             [59, 73],
#             [35, 32],
#             [40, 31],
#             [14, 31],
#             [71, 35],
#             [96, 18],
#             [27, 39],
#             [28, 38],
#             [41, 36],
#             [31, 63],
#             [52, 48],
#             [81, 25],
#             [49, 90],
#             [32, 65],
#             [25, 45],
#             [63, 94],
#             [89, 50],
#             [43, 41]
# ]
print(queensAttack(n, k, r_q, c_q, obstacles))
# 40
