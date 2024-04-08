"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
1249. Minimum Remove to Make Valid Parentheses
Medium

4143

71

Add to List

Share
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        level = 0
        if s == "":
            return ""
        for i in range(len(s)):
            if s[i] == ')' and level == 0:
                continue
            elif s[i] == '(':
                level += 1
                stack.append(s[i])
            elif s[i] == ')':
                level -= 0
                stack.append(s[i])
            else:
                stack.append(s[i])
        res = ""
        if level != 0:
            for i in range(len(stack)-1, -1, -1):
                if stack[i] == '(' and level != 0:
                    level -= 1
                    continue
                else:
                    res = stack[i] + res
        else:
            for i in range(len(stack)-1, -1, -1):
                res = stack[i] + res
        return res
