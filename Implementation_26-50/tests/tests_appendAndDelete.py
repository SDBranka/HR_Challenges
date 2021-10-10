import unittest
import sys
sys.path.append("..")
from implementation import appendAndDelete


class test_appendAndDelete(unittest.TestCase):
    def testExample(self):
        s = ["a", "b", "c"]
        t = ["d", "e", "f"]
        k = 6
        self.assertEqual(appendAndDelete(s, t, k), "Yes")

    def testZero(self):
        s = ["h", "a", "c", "k", "e", "r", "h", "a", "p", "p", "y"]
        t = ["h", "a", "c", "k", "e", "r", "r", "a", "n", "k"]
        k = 9
        self.assertEqual(appendAndDelete(s, t, k), "Yes")

    def testOne(self):
        s = ["a", "b", "a"]
        t = ["a", "b", "a"]
        k = 7
        self.assertEqual(appendAndDelete(s, t, k), "Yes")

    def testTwo(self):
        s = ["a", "s", "h", "l", "e", "y"]
        t = ["a", "s", "h"]
        k = 2
        self.assertEqual(appendAndDelete(s, t, k), "No")

    def testFour(self):
        s = ["q", "w", "e", "r", "a", "s", "d", "f"]
        t = ["q", "w", "e", "r", "b", "s", "d", "f"]
        k = 6
        self.assertEqual(appendAndDelete(s, t, k), "No")

    def testFive(self):
        s = ["y"]
        t = ["y", "u"]
        k = 2
        self.assertEqual(appendAndDelete(s, t, k), "No")

    def testEight(self):
        s = ["a", "s", "d", "f", "q", "w", "e", "r", "t", 
            "y", "u", "i", "g", "h", "j", "k", "z", "x",
            "c", "v", "a", "s", "d", "f", "q", "w", "e", 
            "r", "t", "y", "u", "i", "g", "h", "j", "k",
            "z", "x", "c", "v", "a", "s", "d", "f", "q",
            "w", "e", "r", "t", "y", "u", "i", "g", "h", 
            "j", "k", "z", "x", "c", "v", "a", "s", "d", 
            "f", "q", "w", "e", "r", "t", "y", "u", "i", 
            "g", "h", "j", "k", "z", "x", "c", "v", "a", 
            "s", "d", "f", "q", "w", "e", "r", "t", "y", 
            "u", "i", "g", "h", "j", "k", "z", "x", "c", 
            "v"]
        t = ["b", "s", "d", "f", "q", "w", "e", "r", "t", 
            "y", "u", "i", "g", "h", "j", "k", "z", "x", 
            "c", "v", "a", "s", "d", "f", "q", "w", "e", 
            "r", "t", "y", "u", "i", "g", "h", "j", "k", 
            "z", "x", "c", "v", "a", "s", "d", "f", "q", 
            "w", "e", "r", "t", "y", "u", "i", "g", "h", 
            "j", "k", "z", "x", "c", "v", "a", "s", "d", 
            "f", "q", "w", "e", "r", "t", "y", "u", "i", 
            "g", "h", "j", "k", "z", "x", "c", "v", "a", 
            "s", "d", "f", "q", "w", "e", "r", "t", "y", 
            "u", "i", "g", "h", "j", "k", "z", "x", "c", 
            "v"]
        k = 100
        self.assertEqual(appendAndDelete(s, t, k), "No")

    def testThree(self):
        s = ["z", "z", "z", "z", "z"]
        t = ["z", "z", "z", "z", "z", "z", "z"]
        k = 4
        self.assertEqual(appendAndDelete(s, t, k), "Yes")

    def testTen(self):
        s = ["a", "b", "c", "d"]
        t = ["a", "b", "c", "d", "e", "r", "t"]
        k = 10
        self.assertEqual(appendAndDelete(s, t, k), "No")


if __name__ == '__main__':
    unittest.main()       



# #5 Append and Delete
# https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# You have two strings of lowercase English letters. 
# You can perform two types of operations on the 
# first string:
#     1. Append a lowercase English letter to the 
#           end of the string.
#     2. Delete the last character of the string. 
#           Performing this operation on an empty 
#           string results in an empty string.
# Given an integer, k, and two strings, s and t, 
# determine whether or not you can convert s to t by 
# performing exactly k of the above operations on s.
# If it's possible, print Yes. Otherwise, print No.

# Example.
# s = [a, b, c]
# t = [d, e, f]
# k = 6
# To convert s to t, we first delete all of the 
# characters in 3 moves. Next we add each of the 
# characters of t in order. On the 6th move, you will 
# have the matching string. Return Yes.
# If there were more moves available, they could have
# been eliminated by performing multiple deletions on
# an empty string. If there were fewer than 6moves, 
# we would not have succeeded in creating the new 
# string.

# Function Description
# Complete the appendAndDelete function in the editor
#   below. It should return a string, 
#   either Yes or No.
# appendAndDelete has the following parameter(s):
#     string s: the initial string
#     string t: the desired string
#     int k: the exact number of operations that must be performed

# Returns
#     string: either Yes or No

# Input Format
# The first line contains a string s, the initial 
#   string.
# The second line contains a string t, the desired 
#   final string.
# The third line contains an integer k, the number 
#   of operations.

# Constraints
#   1 <= |s| <= 100
#   1 <= |t| <= 100
#   1 <= k <= 100
#   s and t consist of lowercase English letters, ascii[a-z]    .

# Sample Input 0
# hackerhappy
# hackerrank
# 9
# Sample Output 0
# Yes
# Explanation 0
# We perform 5 delete operations to reduce string s 
# to hacker. Next, we perform 4 append operations 
# (i.e., r, a, n, and k), to get hackerrank. Because
# we were able to convert s to t by performing 
# exactly k = 9 operations, we return Yes.

# Sample Input 1
# aba
# aba
# 7
# Sample Output 1
# Yes
# Explanation 1
# We perform 4 delete operations to reduce string s 
# to the empty string. Recall that though the string
# will be empty after 3 deletions, we can still 
# perform a delete operation on an empty string to 
# get the empty string. Next, we perform 3 append 
# operations (i.e., a, b, and a). Because we were 
# able to convert to by performing exactly k = 7
# operations, we return Yes.

# Sample Input 2
# ashley
# ash
# 2
# Sample Output 2
# No
# Explanation 2
# To convert ashley to ash a minimum of 3 steps are 
# needed. Hence we print No as answer. 
