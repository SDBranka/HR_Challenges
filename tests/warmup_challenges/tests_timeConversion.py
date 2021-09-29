import io
import unittest
import unittest.mock
import sys
sys.path.append("../..")
from warmup_challenges import timeConversion


class test_miniMaxSum0(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        timeConversion(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        s = "12:01:00AM"
        self.assert_stdout(s, "00:01:00")

    def testTwo(self):
        s = "12:01:00PM"
        self.assert_stdout(s, "12:01:00")

    def testThree(self):
        s = "02:01:00AM"
        self.assert_stdout(s, "02:01:00")

    def testFour(self):
        s = "10:01:00PM"
        self.assert_stdout(s, "22:01:00")



if __name__ == '__main__':
    unittest.main()       



# #10 Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Given a time in 12 hour AM/PM format, convert it to 
# military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 
# 24-hour clock. 12:00:00PM on a 12-hour clock is 
# 12:00:00 on a 24-hour clock.

# Example
# s = "12:01:00PM"
# Return '12:01:00'.
# s = "12:01:00AM"
# Return '00:01:00'.

# Function Description
# Complete the timeConversion function in the editor below. 
# It should return a new string representing the input time 
# in 24 hour format.
# timeConversion has the following parameter(s):
#     string s: a time in 12 hour format

# Returns
#     string: the time in 24 hour format

# Input Format
# A single string s that represents a time in 12-hour 
# clock format (i.e.: or).

# Constraints
#     All input times are valid

# Sample Input 0
# 07:05:45PM
# Sample Output 0
# 19:05:45
