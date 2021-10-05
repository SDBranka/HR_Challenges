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
    # gather the quantity of each type of bird
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
        # the first one found will be the lowest type value
        if bird_dict[key] == max(bird_dict.values()):
            key_split = key.split()
            # print(key_split)
            # return the integer of the key that corresponds to the highest number of birds in that type
            return int(key_split[1])


# 11
def dayOfProgrammer0(year):
    # sum the days of the month from jan -> aug - feb (31 + 31 + 30 + 31 + 30 + 31 + 31)
    base_day_count = 215

    # determine if it was a leap year and add feb to the day count
    if (year <= 1917 and year %4 == 0)\
        or (year % 400 == 0)\
        or (year % 4 == 0 and (year % 100 != 0)):    
        base_day_count += 29
    elif year == 1918:
        base_day_count += 15
    else:
        base_day_count += 28

    # find the 256 day
    prog_day = ".09."
    date_str = 256 - base_day_count
    year_str = str(year)
    # concantenate return string
    prog_day = f"{date_str}{prog_day}{year_str}"
    return prog_day


def dayOfProgrammer1(year):
    if (year == 1918):
        return "26.09.1918"
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year


# 12
def bonAppetit(bill, k, b):
    b_actual = (sum(bill) - bill[k]) / 2

    if b > b_actual:
        print(round(b - b_actual))
    else:
        print("Bon Appetit")


# 13
def pageCount(n, p):
    # make a book
    # print(tuple(range(0, n + 1, 1)))
    if n % 2 != 0:
        book_max = n + 1
    else:
        book_max = n + 2
    book = (tuple(range(0, book_max, 1)))
    forward_turn_count = 0
    backward_turn_count = 0

    # forward count
    i = 0
    while i <= n:
        if book[i] == p or book[i+1] == p:
            # print("front found")
            break
        else:
            forward_turn_count +=1
            i += 2
    # print(forward_turn_count)

    # backward count
    i = n
    # if odd number of pages
    if n % 2 != 0:
        i -= 1
    while n >= 0:
        if book[i] == p or book[i+1] == p:
            # print("back found")
            break
        else:
            backward_turn_count += 1
            i -=2
    # print(f"back = {backward_turn_count}")
    # print(min(forward_turn_count, backward_turn_count))

    return min(forward_turn_count, backward_turn_count)


# 14
def catAndMouse(x, y, z):
    if abs(x-z) == abs(y-z):
        return "Mouse C"
    elif abs(x-z) < abs(y-z):
        return "Cat A"
    else:
        return "Cat B"


# 15
# def formingMagicSquare(s):
# not complete


# 16
# I originally solved for consecutive index locations
def findSliceLength0(arr_to_check):
    # print(f"arr_to_check = {arr_to_check}")
    i = 0
    check_pos = arr_to_check[0]
    print(f"check_pos = {check_pos}")
    # n = len(arr_to_check)
    # if i < n-1:
        # print(f"abs val check = {abs(check_pos - arr_to_check[i+1])}")
    max_count = 0
    while i < len(arr_to_check) and\
        (arr_to_check[i] == check_pos\
            or abs(check_pos - arr_to_check[i]) == 1):  
        print(f"max_count = {max_count}")
        max_count += 1
        i += 1
    return max_count

def pickingNumbers0(a):
    n = len(a)
    # find sets
    j = 0
    max_count_arr = []
    while j < n:
        print(f"j = {j}")
        check_arr = a[j:n]
        # print(check_arr)
        max_count_arr.append(findSliceLength0(check_arr))
        j += 1
    # print(max_count_arr)    
    return max(max_count_arr)

def pickingNumbers(a):
    set_a = list(set(a))
    n = len(set_a)
    max_count_arr = []
    if n == 0:
        return 0
    elif n == 1:
        return a.count(set_a[0])
    else:
        for i in range(n - 1):
            max_count = 0   
            check_a = set_a[i]
            abs_val_check = abs(check_a - set_a[i + 1])
            if abs_val_check == 1:
                max_count += a.count(set_a[i + 1]) +  a.count(check_a)
            else:
                max_count +=  a.count(check_a)
            max_count_arr.append(max_count)
    
    return max(max_count_arr)


# 17
def climbingLeaderboard0(ranked, player):
    set_ranked = sorted(list(set(ranked)), reverse=True)
    # print(set_ranked)
    player_ranks = []
    for score in player:
        if score not in set_ranked:
            set_ranked.append(score)
            set_ranked = sorted(set_ranked, reverse=True)
            # print(set_ranked)
        player_ranks.append(set_ranked.index(score) + 1)
        set_ranked = set_ranked[:set_ranked.index(score)]
        # print(f"set_ranked = {set_ranked}")
    return player_ranks

def climbingLeaderboard1(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l=len(ranked)
    j=0
    
    ans=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1        
        ans.append(j+1)
        
    return ans[::-1]


# 18
def hurdleRace(k, height):
    max_h = max(height)
    if k >= max_h:
        return 0
    else:
        return  max(height) - k


# 19
def designerPdfViewer(h, word):
    alpha_list = [
        "a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y",
        "z"
    ]

    heights_list = []
    for letter in word:
        heights_list.append(h[alpha_list.index(letter)])
    return len(word) * max(heights_list)


# 20
def utopianTree(n):
    sap_height = 1
    if n == 0:
        return sap_height
    for i in range(1, n + 1):
        print(f"i = {i}")
        if i % 2 != 0:
            sap_height *= 2
        else:
            sap_height += 1
    return sap_height


# 21
# for some reason on the site it would only accept my answer if the returns were reversed
def angryProfessor(k, a):
    count = 0
    for student in a:
        if student <= 0:
            count += 1
    if count >= k:
        return "YES"
    else:
        return "NO"


# 22
