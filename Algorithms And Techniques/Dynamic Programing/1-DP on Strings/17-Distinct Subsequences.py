"""

https://leetcode.com/problems/distinct-subsequences/description/

115. Distinct Subsequences
Hard
Topics

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        def dp(i,j):
            if j == 0:
                return 1
            if i == 0 and j != 0:
                return 0
            if s[i-1] == t[j-1]:
                return dp(i-1,j-1) + dp(i-1,j)
            return dp(i-1,j)

        return dp(N,M)

model = Solution()
print(model.numDistinct("babgbag","bag"))