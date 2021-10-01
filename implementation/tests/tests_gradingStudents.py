import unittest
import sys
sys.path.append("../..")
from implementation import gradingStudents


class test_gradingStudents(unittest.TestCase):
    def testZero(self):
        grades = [75, 67, 40, 33]
        self.assertEqual(gradingStudents(grades), [75, 67, 40, 33])

    def testThree(self):
        grades = [84, 94, 21, 0, 18, 100,18, 62, 30, 61, 53, 0, 
                    43, 2, 29, 53, 61, 40, 14, 4, 29, 98, 37, 23, 
                    46, 9, 79, 62, 20, 38, 51, 99, 59, 47, 4, 86, 
                    61, 68, 17, 45, 6, 1, 95, 95]
        self.assertEqual(gradingStudents(grades), [85, 95, 21, 0, 18, 100, 18, 62, 30, 61, 
                                                    55, 0, 45, 2, 29, 55, 61, 40, 14, 4, 29, 
                                                    100, 37, 23, 46, 9, 80, 62, 20, 40, 51, 
                                                    100, 60, 47, 4, 86, 61, 70, 17, 45, 6, 1, 
                                                    95, 95]
                                                    )



if __name__ == '__main__':
    unittest.main()       



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

