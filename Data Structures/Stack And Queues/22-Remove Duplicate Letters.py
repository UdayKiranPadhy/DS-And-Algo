"""

316. Remove Duplicate Letters
Medium

https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


https://www.youtube.com/watch?v=bOTjexiYtJo

"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {c: i for i, c in enumerate(s)}

        seen = set()
        stack = []
        for i, c in enumerate(s):
            # empty stack
            if len(stack) == 0:
                stack.append(c)
                seen.add(c)
                continue

            # char is in leco order
            if c in seen:
                continue
            while stack and stack[-1] > c and i < last_seen[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        res = "".join(stack)
        return res

