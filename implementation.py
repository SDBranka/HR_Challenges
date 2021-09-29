# #1 Grading Students
# https://www.hackerrank.com/challenges/grading/problem
# HackerLand University has the following grading policy:
# Every student receives a grade in the inclusive range 
# from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round 
# each student's grade according to these rules:
# -If the difference between the grade and the next 
#  multiple of 5 is less than 3, round up to the next 
#  multiple of 5.
# -If the value of grade is less than 38, no rounding 
#  occurs as the result will still be a failing grade.

# Examples
# grade = 84 round to 85 (85 - 84 is less than 3)
# grade = 29 do not round (result is less than 40)
# grade = 57 do not round (60 - 57 is 3 or higher)

# Given the initial value of grade for each of Sam's n
# students, write code to automate the rounding process.

# Function Description
# Complete the function gradingStudents in the editor below.
# gradingStudents has the following parameter(s):
#     int grades[n]: the grades before rounding

# Returns
#     int[n]: the grades after rounding as appropriate

# Input Format
# The first line contains a single integer, n, the number 
# of students.Each line of the subsequent lines contains 
# a single integer, grades[i].

# Constraints
# 1 <= n <= 60
# 0 <= grades[i] <= 100

# Sample Input 0
# 4
# 73
# 67
# 38
# 33
# Sample Output 0
# 75
# 67
# 40
# 33
# Explanation 0
    # id      Orig_Grade      Final_grade
    # 1           73              75
    # 2           67              67  
    # 3           38              40
    # 4           33              33

# Student 1 received a 73, and the next multiple of 5 from 
# 73 is 75. Since 75 - 73 < 3, the student's grade is 
# rounded to 75.
# Student 2 received a 67, and the next multiple of 5 from 
# 67 is 70. Since 70 - 67 = 3, the grade will not be modified
# and the student's final grade is 67.
# Student 3 received a 38, and the next multiple of 5 from 
# 38 is 40. Since 40 - 38 < 3, the student's grade will be
# rounded to 40.
# Student 4 received a grade below 33, so the grade will 
# not be modified and the student's final grade is 33.

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (((grades[i] // 10) * 10) + 10) - grades[i] < 3:
                grades[i] = ((grades[i]// 10) * 10) +10
            elif (((grades[i] // 10) * 10) + 5) - grades[i] < 3 and (((grades[i] // 10) * 10) + 5) - grades[i] > 0:
                grades[i] = ((grades[i]// 10) * 10) +5
    return grades

# #2 Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen
# Sam's house has an apple tree and an orange tree that
# yield an abundance of fruit. Using the information 
# given below, determine the number of apples and 
# oranges that land on Sam's house.

# In the diagram below:
#     The red region denotes the house, where s is the 
#       start point, and t is the endpoint. The apple 
#       tree is to the left of the house, and the orange 
#       tree is to its right.
#     Assume the trees are located on a single point, 
#       where the apple tree is at point a, and the 
#       orange tree is at point b.
#     When a fruit falls from its tree, it lands d units
#       of distance from its tree of origin along the 
#       x-axis. *A negative value of d means the fruit 
#       fell d units to the tree's left, and a positive 
#       value of means it falls d units to the tree's 
#       right. *

# diagram
# a      s    t       b
# a = apple tree
# s = start point
# t = endpoint
# b = orange tree

# Given the value of d for apples and oranges, determine
# how many apples and oranges will fall on Sam's house 
# (i.e., in the inclusive range [s, t])?

# For example, Sam's house is between s = 7 and t = 10. 
# The apple tree is located at a = 4 and the orange at 
# b = 12. There are m = 3 apples and n = 3 oranges. 
# Apples are thrown apples = [2, 3, -4] units distance 
# from a, and oranges = [3, -2, -4] units distance. 
# Adding each apple distance to the position of the 
# tree, they land at [4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]. 
# Oranges land at [12 + 3, 12 + -2, 12 + -4] = [15, 10, 8].
# One apple and two oranges land in the inclusive range
# 7-10 so we print
# 1
# 2

# Function Description
# Complete the countApplesAndOranges function in the 
#   editor below. It should print the number of apples 
#   and oranges that land on Sam's house, each on a 
#   separate line.
# countApplesAndOranges has the following parameter(s):
#     s: integer, starting point of Sam's house location.
#     t: integer, ending location of Sam's house location.
#     a: integer, location of the Apple tree.
#     b: integer, location of the Orange tree.
#     apples: integer array, distances at which each apple falls from the tree.
#     oranges: integer array, distances at which each orange falls from the tree.

# Input Format
# The first line contains two space-separated integers 
# denoting the respective values of s and t.
# The second line contains two space-separated integers
# denoting the respective values of a and b.
# The third line contains two space-separated integers 
# denoting the respective values of m and n.
# The fourth line contains space-separated integers 
# denoting the respective distances that each apple 
# falls from point a.
# The fifth line contains space-separated integers 
# denoting the respective distances that each orange 
# falls from point b.

# Constraints
# 1 <= s, t, a, b, m, n <= 10^
# -10^5 <= d <= 10^5
# a < s < t < b

# Output Format
# Print two integers on two different lines:
#     The first integer: the number of apples that fall on Sam's house.
#     The second integer: the number of oranges that fall on Sam's house.

# Sample Input 0
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6
# Sample Output 0
# 1
# 1
# Explanation 0
# The first apple falls at position 5 - 2 = 3.
# The second apple falls at position 5 + 2 = 7.
# The third apple falls at position 5 + 1 = 6.
# The first orange falls at position 15 + 5 = 20.
# The second orange falls at position 15 - 6 = 9.
# Only one fruit (the second apple) falls within the 
#   region between 7 and 11, so we print 1 as our first 
#   line of output.
# Only the second orange falls within the region 
#   between 7 and 11, so we print 1 as our second line 
#   of output. 



def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_distances = list(map(lambda x: x + a, apples))
    # print(apple_distances)
    orange_distances = list(map(lambda x: x + b, oranges))
    # print(orange_distances)
    a_count = 0
    for a in apple_distances:
        if a <= t and a >= s:
            a_count += 1
    print(a_count)
    b_count = 0
    for b in orange_distances:
        if b <= t and b >= s:
            b_count += 1
    print(b_count)



# #3 Number Line Jumps
# https://www.hackerrank.com/challenges/kangaroo/problem
# You are choreographing a circus show with various 
# animals. For one act, you are given two kangaroos 
# on a number line ready to jump in the positive 
# direction (i.e, toward positive infinity).
# -The first kangaroo starts at location x1 and moves 
#   at a rate of v1 meters per jump.
# -The second kangaroo starts at location x2 and moves 
#   at a rate of v2 meters per jump.

# You have to figure out a way to get both kangaroos 
# at the same location at the same time as part of the 
# show. If it is possible, return YES, otherwise 
# return NO.

# Example
# x1 = 2
# v1 = 1
# x2 = 1
# v2 = 2
# After one jump, they are both at x-3, 
# (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), so the answer is 
# YES.

# Function Description
# Complete the function kangaroo in the editor below.
# kangaroo has the following parameter(s):
#     int x1, int v1: starting position and jump distance for kangaroo 1
#     int x2, int v2: starting position and jump distance for kangaroo 2

# Returns
#     string: either YES or NO

# Input Format
# A single line of four space-separated integers denoting 
# the respective values of x1, v1, x2, and v2.

# Constraints
# 0 <= x1 < x2 <= 10000
# 1 <= v1 <= 10000
# 1 <= v2 <= 10000

# Sample Input 0
# 0 3 4 2
# Sample Output 0
# YES
# Explanation 0
# The two kangaroos jump through the following sequence 
# of locations:

# image

# From the image, it is clear that the kangaroos meet 
# at the same location (number 12 on the number line) 
# after same number of jumps (4 jumps), and we print YES.

# Sample Input 1
# 0 2 5 3
# Sample Output 1
# NO
# Explanation 1
# The second kangaroo has a starting location that 
# is ahead (further to the right) of the first 
# kangaroo's starting location (i.e. x2 > x1). Because
# the second kangaroo moves at a faster rate (meaning 
# v2 > v1) and is already ahead of the first kangaroo, 
# the first kangaroo will never be able to catch up. 
# Thus, we print NO. 

def kangaroo(x1, v1, x2, v2):
    # 10000
    for i in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
        if i == 9999 and x1 != x2:
            # print("NO")
            return "NO"



# #5 Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Maria plays college basketball and wants to go pro. 
# Each season she maintains a record of her play. She 
# tabulates the number of times she breaks her season 
# record for most points and least points in a game. 
# Points scored in the first game establish her record 
# for the season, and she begins counting from there.

# Example
# score = [12, 24, 10, 24]
# Scores are in the same order as the games played. She 
# tabulates her results as follows:
#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1

# Given the scores for a season, determine the number of
# times Maria breaks her records for most and least 
# points scored during the season.

# Function Description
# Complete the breakingRecords function in the editor 
# below.
# breakingRecords has the following parameter(s):
#     int scores[n]: points scored per game

# Returns
#     int[2]: An array with the numbers of times she 
#       broke her records. Index 0 is for breaking most
#       points records, and index 1 is for breaking 
#       least points records.

# Input Format
# The first line contains an integer n, the number of 
# games. The second line contains n space-separated 
# integers describing the respective values of
# score0...scorei...scoren-1

# Constraints
# 1 <= n <= 1000
# 0 <= score[i] <=10^8

# Sample Input 0
# 9
# 10 5 20 20 4 5 2 25 1
# Sample Output 0
# 2 4
# Explanation 0
# The diagram below depicts the number of times Maria
# broke her best and worst records throughout the 
# season:

# Game          0   1   2   3   4   5   6   7   8
# Score         10  5   20  20  4   5   2   25  1
# High Score    10  10  20  20  20  20  20  25  25  
# Low Score     10  5   5   5   4   4   2   2   1

# She broke her best record twice (after games 2and 7)
# and her worst record four times (after games 1, 4, 6,
# and 8), so we print 2 4 as our answer. Note that she
# did not break her record for best score during game 3,
# as her score during that game was not strictly 
# greater than her best record at the time.

# Sample Input 1
# 10
# 3 4 21 36 10 28 35 5 24 42
# Sample Output 1
# 4 0
# Explanation 1
# The diagram below depicts the number of times Maria
# broke her best and worst records throughout the 
# season:

# Game          0   1   2   3   4   5   6   7   8   9
# Score         3   4   21  36  10  28  35  5   24  42
# High Score    3   4   21  36  36  36  36  36  36  42  
# Low Score     3   3   3   3   3   3   3   3   3   3

# She broke her best record four times (after games
# 1, 2, 3, and 9) and her worst record zero times (no
# score during the season was lower than the one she 
# earned during her first game), so we print 4 0 as 
# our answer.

def breakingRecords(scores):
    max_score = scores[0]
    max_count = 0
    min_score = scores[0]
    min_count = 0
    
    for score in scores:
        if score < min_score :
            min_score = score
            min_count += 1
        elif score > max_score:
            max_score = score
            max_count += 1

    return [max_count, min_count]





