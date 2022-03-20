"""

1081. Smallest Subsequence of Distinct Characters
Medium

1569

140

Add to List

Share
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/


"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_seen = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last_seen[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return "".join(stack)
