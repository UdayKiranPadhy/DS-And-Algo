"""

 Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the 
length of the longest valid (well-formed) parentheses substring.


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""

# Problem statement
# https://leetcode.com/problems/longest-valid-parentheses/

# Solution
# This is quite difficult problem, which can be solved with dymamic programming.
# As usual let us define dp[i] the length of the longest valid substring ending
# at i-th index. We can have several cases now:

# If i == -1, it means we reached empty string, return 0, answer for empty string.
# Also if s[i] = (, answer is also 0, because no valid parantheses can end with (
# Now, we have case, when s[i] = ). Let us look at the previous element.
# If it is equal to (, then we have () as two last elements and we can return dp(i-2) + 2.
# Now consider the case, when s[i-1] = ), it means, that we have the following
# situation: ...)). If we want to find the longest valid parentheses for i, first
# we need to deal with i-1. Define P = i - dp(i-1) - 1. Then we have the following situation:
# ...((.....))

# ...P.......i

# Here on the top is the structure of string and in the bottom are indexes.
# String from P + 1 to i - 1 indexes including is the longest valid parentheses
# endind with i-1 place. What we can say about place P. If we have ) element on this place,
# then we need to return 0: in this case we have patten ...)(...))... and we know that
# answer for dp(P) is equal to 0: if it is not, what we considered was not the longest
# answer for i-1. And if answer for dp(P) is zero, than answer for dp(i) is zero as well.
# In the case, when we have ...((.....)), answer is dp(i-1) + dp(P-1) + 2.

# Complexity
# Time complexity is O(n), space complexity as well.

from functools import lru_cache


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        @lru_cache(None)
        def dp(i):
            if i <= 0 or dp[i] == '(':
                return 0
            if i >= 1 and s[i-1:i+1] == "()":
                return dp(i-2) + 2
            if s[i-1] == ')':
                P = i-dp(i-1) - 1
                if s[P] == '(':
                    return dp[i-1]+dp[P-1] + 2
            return 0

        return max(dp(i) for i in range(len(s))) if s else 0


# Wont Work
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        level = 0
        score = 0
        best = 0
        for i in range(len(s)):

            if s[i] == '(':
                level += 1
            else:
                if level <= 0:
                    score = 0
                    level = 0
                    continue
                level -= 1
                score += 2
                best = max(best, score)

        return best
