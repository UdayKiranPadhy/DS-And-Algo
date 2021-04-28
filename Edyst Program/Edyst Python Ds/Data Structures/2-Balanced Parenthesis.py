"""
Balanced Parantheses in Expression
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given a string s, determine whether s is balanced.
If a string is balanced, return 1. Otherwise, return 0.

Example :
Input :
A : {[()]}
B : {[(])}
Output :
A : 1
B : 0
"""


class Solution:
    def isBalanced(self, s):
        stack = []
        closing = {"[": "]", "{": "}", "(": ")"}
        count = 0
        for i in s:
            count += 1
            if i in "[({":
                stack.append(i)
            if i in "])}":
                if len(stack) != 0:
                    braket = stack.pop()
                    if closing[braket] == i:
                        continue
                    else:
                        return 0
                        break
                else:
                    return 0
                    break
        else:
            if len(stack) == 0:
                return 1
            else:
                return 0