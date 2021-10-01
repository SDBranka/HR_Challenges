import unittest
import io
import sys
sys.path.append("../..")
from implementation import bonAppetit


class test_bonAppetit(unittest.TestCase):
    def testExample1(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        k = 2
        bill = [2, 4, 6]
        b = 3
        bonAppetit(bill, k, b)                                   # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        print ('Captured', capturedOutput.getvalue())   # Now works as before.
        ans = "Bon Appetit\n"
        self.assertEqual(capturedOutput.getvalue(), ans)

    def testExample2(self):
        k = 2
        bill = [2, 4, 6]
        b = 6
        self.assertEqual(bonAppetit(bill, k, b), 3)

    def testZero(self):
        k = 1
        bill = [3, 10, 2, 9]
        b = 12
        self.assertEqual(bonAppetit(bill, k, b), 5)

    def testOne(self):
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        k = 1
        bill = [3, 10, 2, 9]
        b = 7
        bonAppetit(bill, k, b)                                  
        sys.stdout = sys.__stdout__                     
        print ('Captured', capturedOutput.getvalue())   
        ans = "Bon Appetit\n"
        self.assertEqual(capturedOutput.getvalue(), ans)



if __name__ == '__main__':
    unittest.main()       



# #12 Bill Division
# https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Two friends Anna and Brian, are deciding how to split
# the bill at a dinner. Each will only pay for the 
# items they consume. Brian gets the check and 
# calculates Anna's portion. You must determine if his
# calculation is correct.

# For example, assume the bill has the following 
# prices: bill = [2, 4, 6]. Anna declines to eat item
# k = bill[2] which costs 6. If Brian calculates the 
# bill correctly, Anna will pay (2 + 4)/2 = 3. If he 
# includes the cost ofbill[2], he will calculate 
# (2 + 4 + 6) / 2 = 6. In the second case, he should 
# refund 3 to Anna.

# Function Description
# Complete the bonAppetit function in the editor below.
# It should print Bon Appetit if the bill is fairly 
# split. Otherwise, it should print the integer amount
# of money that Brian owes Anna.
# bonAppetit has the following parameter(s):
#     bill: an array of integers representing the cost
#       of each item ordered
#     k: an integer representing the zero-based index 
#       of the item Anna doesn't eat
#     b: the amount of money that Anna contributed to 
#       the bill

# Input Format
# The first line contains two space-separated integers
#   n and k, the number of items ordered and the 
#   0-based index of the item that Anna did not eat.
# The second line contains n space-separated integers
#   where 0 <= i < n.
# The third line contains an integer, b, the amount of
#   money that Brian charged Anna for her share of the
#   bill.

# Constraints
#  2 <= n <= 10^5
#  0 <= k <= n
#  0 <= bill[i] <= 10^4
#  0 <= b <= the sum of all of the elements in bill
#  The amount of money due Anna will always be an integer

# Output Format
# If Brian did not overcharge Anna, print Bon Appetit
# on a new line; otherwise, print the difference 
# (i.e., b_charged - b_actual) that Brian must refund to
# Anna. This will always be an integer.

# Sample Input 0
# 4 1
# 3 10 2 9
# 12
# Sample Output 0
# 5
# Explanation 0
# Anna didn't eat item bill[1] = 10, but she shared the
# rest of the items with Brian. The total cost of the
# shared items is 3 + 2 + 9 = 14 and, split in half, the
# cost per person is b_actual = 7. Brian charged her 
# bill_charged = 12 for her portion of the bill. We 
# print the amount Anna was overcharged, 
# b_charged - b_actual = 12 - 7 = 5, on a new line.

# Sample Input 1
# 4 1
# 3 10 2 9
# 7
# Sample Output 1
# Bon Appetit
# Explanation 1
# Anna didn't eat item bill[1] = 10, but she shared the 
# rest of the items with Brian. The total cost of the 
# shared items is 3 + 2 + 9 = 14 and, split in half, the
# cost per person is b_actual = 7. Because 
# b_actual - b_charged = 7, we print Bon Appetit on a 
# new line. 
