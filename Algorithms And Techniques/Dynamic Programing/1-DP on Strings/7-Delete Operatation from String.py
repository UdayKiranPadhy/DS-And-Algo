"""
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and 
word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 
Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


# Solution
"""
STEP 1: Understand the problem.
Quick explanation: We can delete a character in either string in each move to make both string equal. 
Return minimum no. of moves.

STEP 2: Base Cases
Both strings are empty: 0
One string is empty. We have to delete all the character in other string to make it empty. 
So min. no of moves has to be equal to the length of the non-empty string.

STEP 3: Definition of problem.
If both characters are same. We dont have to delete it, so the moves will be equal to subproblem with state(i -1, j - 1)
If both characters are not the same. We can delete character from either string. So the min no of moves has to be minimum between dp[i][j - 1] and dp[i - 1][j].
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        cost = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    cost[i][j] = j
                elif j == 0:
                    cost[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    cost[i][j] = cost[i - 1][j - 1]
                else:
                    cost[i][j] = 1 + min(cost[i - 1][j], cost[i][j - 1])
        return cost[-1][-1]


# https://leetcode.com/problems/delete-operation-for-two-strings/
