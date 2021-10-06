import unittest
import sys
sys.path.append("..")
from implementation import climbingLeaderboard0, climbingLeaderboard1


class test_climbingLeaderboard0(unittest.TestCase):
    def testExample(self):
        ranked = [100, 90, 90, 80]
        player = [70, 80, 105]
        self.assertEqual(climbingLeaderboard0(ranked, player), [4, 3, 1])

    def testOne(self):
        ranked = [100, 100, 50, 40, 40, 20, 10]
        player = [5, 25, 50, 120]
        self.assertEqual(climbingLeaderboard0(ranked, player), [6, 4, 2, 1])

    def testTwo(self):
        ranked = [100, 90, 90, 80, 75, 60]
        player = [50, 65, 77, 90, 102]
        self.assertEqual(climbingLeaderboard0(ranked, player), [6, 5, 4, 2, 1])

class test_climbingLeaderboard1(unittest.TestCase):
    def testExample(self):
        ranked = [100, 90, 90, 80]
        player = [70, 80, 105]
        self.assertEqual(climbingLeaderboard1(ranked, player), [4, 3, 1])

    def testOne(self):
        ranked = [100, 100, 50, 40, 40, 20, 10]
        player = [5, 25, 50, 120]
        self.assertEqual(climbingLeaderboard1(ranked, player), [6, 4, 2, 1])

    def testTwo(self):
        ranked = [100, 90, 90, 80, 75, 60]
        player = [50, 65, 77, 90, 102]
        self.assertEqual(climbingLeaderboard1(ranked, player), [6, 5, 4, 2, 1])


if __name__ == '__main__':
    unittest.main()       



# #17 Climbing the Leaderboard
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_v=zen
# An arcade game player wants to climb to the top of the 
# leaderboard and track their ranking. The game uses Dense 
# Ranking, so its leaderboard works like this:
#     The player with the highest score is ranked number 1
#     on the leaderboard.
#     Players who have equal scores receive the same ranking 
#       number, and the next player(s) receive the immediately
#       following ranking number.

# Example
# ranked = [100, 90, 90, 80]
# player = [70, 80, 105]
# The ranked players will have ranks 1, 2, 2, and 3, 
# respectively. If the player's scores are 70, 80, and 105,
# their rankings after each game are 4th, 3rd and 1st. 
# Return [4, 3, 1].

# Function Description
# Complete the climbingLeaderboard function in the 
# editor below.
# climbingLeaderboard has the following parameter(s):
#     int ranked[n]: the leaderboard scores
#     int player[m]: the player's scores

# Returns
#     int[m]: the player's rank after each new score

# Input Format
# The first line contains an integer n, the number of
#   players on the leaderboard.
# The next line contains n space-separated integers 
#   ranked[i], the leaderboard scores in decreasing order.
# The next line contains an integer, m, the number games
#   the player plays.
# The last line contains m space-separated integers 
# player[j], the game scores.

# Constraints
#   1 <= n <= 2*10^5
#   1 <= m <= 2*10^5
#   0 <= ranked[i] <= 10^9 for 0 <= i < n
#   0 <= player[j] <= 10^9 for 0 <= j < m
#  The existing leaderboard,ranked, is in descending 
#   order.
# The player's scores, player, are in ascending order.

# Subtask
# For 60% of the maximum score:
#   1 <= n <= 200
#   1 <= m <= 200

# Sample Input 1
# ranked = [100, 100, 50, 40, 40, 20, 10]
# player = [5, 25, 50, 120]
# Sample Output 1
# 6
# 4
# 2
# 1
# Explanation 1
# Alice starts playing with 7 players already on the 
# leaderboard, which looks like this:
# Rank      Name        Score
#  1        Emma        100
#  1        David       100
#  2        Caroline    50
#  3        Ritka       40
#  3        Tom         40
#  4        Heraldo     20
#  5        Riley       10
# After Alice finishes game 0, her score is 5 and her 
# ranking is 6:
# Rank      Name        Score
#  1        Emma        100
#  1        David       100
#  2        Caroline    50
#  3        Ritka       40
#  3        Tom         40
#  4        Heraldo     20
#  5        Riley       10
#  6        Alice       5
# After Alice finishes game 1, her score is 25 and her
# ranking is 4:
# Rank      Name        Score
#  1        Emma        100
#  1        David       100
#  2        Caroline    50
#  3        Ritka       40
#  3        Tom         40
#  4        Alice       25
#  5        Heraldo     20
#  6        Riley       10

# After Alice finishes game 2, her score is 50 and her
# ranking is tied with Caroline at 2:
# Rank      Name        Score
#  1        Emma        100
#  1        David       100
#  2        Caroline    50
#  2        Alice       50
#  3        Ritka       40
#  3        Tom         40
#  4        Heraldo     20
#  5        Riley       10

# After Alice finishes game 3, her score is 120 and 
# her ranking is 1:
# Rank      Name        Score
#  1        Alice       120
#  2        Emma        100
#  2        David       100
#  3        Caroline    50
#  4        Ritka       40
#  4        Tom         40
#  5        Heraldo     20
#  6        Riley       10

# Sample Input 2
# ranked = [100, 90, 90, 80, 75, 60]
# player = [50, 65, 77, 90, 102]
# Sample Output 2
# 6
# 5
# 4
# 2
# 1
