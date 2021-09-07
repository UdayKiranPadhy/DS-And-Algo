"""

44. Wildcard Matching
Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false
 
Example 6:

Input: s = "", p = "********"
Output: True

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""

# Problem statement
# https://leetcode.com/problems/wildcard-matching/

# Solution
# Another classical DP problem, similar to problem 0010 Regular Expression Matching. Let us define by dp(i, j)
# answer to the question if s[:i+1] and p[:j+1] can be matched. Then we can have
# different cases:

# if i == -1 and j == -1 it means, that we reached both empty strings, we return True.
# if i == -1, it means, that s string is empty (and t is not empty), in this case we are
# happy only if all symbols of p are equal to *, so we check last symbol check dp(i, j-1).
# if j == -1, but i is not equal to -1, we already checked it previously, we return False.
# if s[i] == p[j], that is last symbols are equal, we remove them and go to dp(i-1, j-1)
# if p[j] not equal to ? or * (that is it is letter) and it is not equal to s[i], we can
# not match, so we return False.
# if p[j] is equal to ?, we can match in only one way and we again go to dp(i-1, j-1).
# finally, if we have * as p[j], we can have two options: we either say that this * is
# finished already, so we delete it, or not finished yet, then we delete symbol from s.

# Complexity
# Complexity: time and space complexity is O(mn).

from functools import lru_cache


class Solution:
    def isMatch(self, s, p):
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1:
                return True
            if i == -1:
                return dp(i, j-1) and p[j] == "*"
            if j == -1:
                return False

            if s[i] == p[j]:
                return dp(i-1, j-1)
            if s[i] != p[j] and p[j] not in "?*":
                return False
            if p[j] == "?":
                return dp(i-1, j-1)
            if p[j] == "*":
                return dp(i-1, j) or dp(i, j-1)

        return dp(len(s) - 1, len(p) - 1)


# My Solution


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def match(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i >= len(s) and p[j] == "*":
                return match(i, j+1)
            if i >= len(s):
                return False
            if s[i] == p[j] or p[j] == '?':
                return match(i+1, j+1)
            if p[j] == "*":
                return match(i+1, j) or match(i+1, j+1) or match(i, j+1)
            return False

        return match(0, 0)


s = input()
p = input()
model = Solution()
print(model.isMatch(s, p))
