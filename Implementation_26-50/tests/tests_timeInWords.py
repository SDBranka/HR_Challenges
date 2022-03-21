import unittest
import sys
sys.path.append("..")
from implementation import timeInWords


class test_timeInWords(unittest.TestCase):
    def testSelfCase0(self):
        h = 5
        m = 30
        self.assertEqual(timeInWords(h, m), "half past five")

    def testSelfCase1(self):
        h = 11
        m = 59
        self.assertEqual(timeInWords(h, m), "one minute to twelve")

    def testSelfCase2(self):
        h = 11
        m = 45
        self.assertEqual(timeInWords(h, m), "quarter to twelve")

    def testSelfCase3(self):
        h = 14
        m = 1
        self.assertEqual(timeInWords(h, m), "one minute past four")

    def testSampleCase0(self):
        h = 5
        m = 47
        self.assertEqual(timeInWords(h, m), "thirteen minutes to six")

    def testSampleCase1(self):
        h = 3
        m = 00
        self.assertEqual(timeInWords(h, m), "three o' clock")

    def testSampleCase2(self):
        h = 7
        m = 15
        self.assertEqual(timeInWords(h, m), "quarter past seven")


if __name__ == '__main__':
    unittest.main()       



# #43
# https://www.hackerrank.com/challenges/the-time-in-words/problem?h_r=next-challenge&h_v=zen
# Given the time in numerals we may convert it into words, as shown below:
# 5:00 -> five o' clock
# 5:01 -> one minute past five
# 5:10 -> ten minutes past five
# 5:15 -> quarter past five
# 5:30 -> half past five
# 5:40 -> twenty minutes to six
# 5:45 -> quarter to six
# 5:47 -> thirteen minutes to six
# 5:28 -> twenty eight minutes past five

# At minutes = 0, use o' clock. For 1 <= minutes <= 30, use past, and for 
# 30 < minutes use to. Note the space between the apostrophe and clock in
# o' clock. Write a program which prints the time in words for the input
# given in the format described.

# Function Description
# Complete the timeInWords function in the editor below.
# timeInWords has the following parameter(s):
# int h: the hour of the day
# int m: the minutes after the hour

# Returns
# string: a time string as described

# Input Format
# The first line contains h, the hours portion. The second line contains m,
# the minutes portion

# Constraints
# - 1 <= h <= 12
# - 0 <= m <= 60

# Sample Input 0
# 5
# 47
# Sample Output 0
# thirteen minutes to six

# Sample Input 1
# 3
# 00
# Sample Output 1
# three o' clock

# Sample Input 2
# 7
# 15
# Sample Output 2
# quarter past seven
