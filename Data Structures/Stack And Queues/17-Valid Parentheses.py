"""



20. Valid Parentheses
Easy

8687

345

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""


# This is very classical problem for using stacks, for me it was literally the
# first problem I saw on this topic. If you know that you need to use stack here,
# it becomes nice and easy.

# What is valid parentheses? It is when we meet some close bracket, it means that
# we need to find corresponding open bracked of the same type. We traverse our s and if we:

# see open bracket we put it to stack
# see closed bracket, then it must be equal to bracket in the top of our stack,
# so we check it and if it is true, we remove this pair of brackets.
# In the end, if and only if we have empty stack, we have valid string.
# Complexity: time complexity is O(n): we put and pop each element of string
# from our stack only once. Space complexity is O(n).

class Solution:
    def isValid(self, s):
        dct = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for char in s:
            if char in dct:
                stack.append(char)
            else:
                if not stack or char != dct[stack.pop()]:
                    return False
        return not stack


# My Solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string = s
        closing = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in string:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    if closing[i] == stack[-1]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
