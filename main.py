# A person wants to determine the most expensive computer
# keyboard and USB drive that can be purchased with a 
# give budget. Given price lists for keyboards and USB 
# drives and a budget, find the cost to buy them. If
# it is not possible to buy both items, return -1.

# Example

# b = 60
# keyboards = [40, 50, 60]
# drives = [5, 8, 12]

# The person can buy a 40 keyboar + 12 USB drive = 52,
# or a 50 keyboard + 8 USB drive = 58.
# Choose the latter as the more expensive option and 
# return 58

# Function Description

# Complete the getMoneySpent function in the editor below.

# getMoneySpent has the following parameter(s):

#     -int keyboards[n]: the keyboard prices
#     -int drives[m]: the drive prices
#     -int b: the budget

# Returns

#     -int: the maximum that can be spent, or -1
#           if it is not possible to buy both items

# Input Format

# The first line contains three space-separated integers
# b, n, and m, the budget, the number of keyboard models 
# and the number of USB drive models.
# The second line contains n space-separated integers 
# keyboard[i], the prices of each keyboard model.
# The third line contains mspace-separated integers
# drives, the prices of the USB drives.

# Constraints

#   1 <= m,n <= 1000
#   1 <= b <= 10^6
#   The price of each item is in the inclusive range [1, 10^6]



# Example:
# Input 0

# 10 2 3
# 3 1
# 5 2 8

# Output 0

# 9

# Explanation 0

# Buy the 2nd keyboard and the 3rd USB drive 
# for a total cost of 8 + 1 = 9.

# Example
# Input 1

# 5 1 1
# 4
# 5

# Output 1

# -1

# Explanation 1

# There is no way to buy one keyboard and one USB drive 
# because 4 + 5 > 5, so return -1.




import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max_budget = 0
    # comparer the prices of each available pair
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            combined_price = keyboards[i] + drives[j]
            # check if they are in the budget
            if combined_price <= b:
                # check if it is greater than the current max_budet
                if combined_price > max_budget:
                    max_budget = combined_price

    # if no items may be purechase return -1
    if max_budget <= 0:
        return -1
    # else return the maximum that may be spent
    return max_budget

b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]
print("###getMoneySpent1")
print(getMoneySpent(keyboards, drives, b))
print("Output: 58")

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]
print("###getMoneySpent2")
print(getMoneySpent(keyboards, drives, b))
print("Output: 9")

b = 5
keyboards = [4]
drives = [5]
print("###getMoneySpent")
print(getMoneySpent(keyboards, drives, b))
print("Output: -1")


# Example:
# Input 0
# the budget
# b = 60
# the number of keyboard models available len(keyboards)
# n = 3
# the number of usb models available len(drives)
# m = 3
# keyboards = [40, 50, 60]
# drives = [5, 8, 12]

# Output 0
# 58

# The person can buy a 40 keyboar + 12 USB drive = 52,
# or a 50 keyboard + 8 USB drive = 58.
# Choose the latter as the more expensive option and 
# return 58



# Example:
# Input 1
# 10 2 3
# 3 1
# 5 2 8

# Output 1
# 9


# Buy the 2nd keyboard and the 3rd USB drive 
# for a total cost of 8 + 1 = 9.



# Example
# Input 2
# 5 1 1
# 4
# 5

# Output 2
# -1
