import math
import os
import random
import re
import sys


# 1
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (((grades[i] // 10) * 10) + 10) - grades[i] < 3:
                grades[i] = ((grades[i]// 10) * 10) + 10
            elif (((grades[i] // 10) * 10) + 5) - grades[i] < 3 and (((grades[i] // 10) * 10) + 5) - grades[i] > 0:
                grades[i] = ((grades[i]// 10) * 10) + 5
    return grades


# 2
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


# 3
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


# 4
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


# 5
def equalizeArray(arr):
    min_num_deletions = 0

    # get singular number occurences
    nums_in_arr = []
    nums_in_arr.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            nums_in_arr.append(arr[i+1])

    # find most prevalent number
    highest_count = 0
    most_of_num = nums_in_arr[0]
    for i in range(len(nums_in_arr)):
        count_num = arr.count(nums_in_arr[i])
        # print(count_num)
        if count_num > highest_count:
            most_of_num = nums_in_arr[i]
            highest_count = count_num
    # count the number of deletions
    for i in range(len(arr)):
        if arr[i] != most_of_num:
            min_num_deletions += 1

    return min_num_deletions


# 6
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


# 7
def birthday(s, d, m):
    count = 0

    if len(s) == 1:
        if s[0] == d:
            count +=1
    elif len(s) > 1:
        if m <= len(s):
            for i in range(len(s) - m + 1):
                # print(f"i+m = {i+m}")
                if sum(s[i:i+m]) == d:
                    count += 1
        else:
            if sum(s) == d:
                count +=1    
    
    return count


# 8
def divisibleSumPairs(n, k, ar):
    pairs = 0

    for i in range(n-1):
        for j in range(n):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    pairs +=1
    return pairs


# 10
def migratoryBirds(arr):
    bird_dict = { "Type 1" : arr.count(1),
                "Type 2" : arr.count(2),
                "Type 3" : arr.count(3),
                "Type 4" : arr.count(4),
                "Type 5" : arr.count(5)
    }
    # print(bird_dict)
    # print(max(bird_dict.values()))

    for key in bird_dict:
        # print(key)
        if bird_dict[key] == max(bird_dict.values()):
            key_split = key.split()
            # print(key_split)
            return int(key_split[1])

