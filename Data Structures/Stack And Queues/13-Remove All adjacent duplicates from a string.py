"""
Date:-28/06/21
Link :- Leetcode


You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca" Output: "ca" Explanation: For example, in "abbaca" we could remove "bb" since the letters are
adjacent and equal, and this is the only possible move. The result of this move is that the string is "aaca",
of which only "aa" is possible, so the final string is "ca". Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.


   Hide Hint #1  
Use a stack to process everything greedily.

"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        stack_top = ''
        index= 0
        while index < len(s):
            if stack_top == s[index]:
                stack.pop()
                index += 1
                if len(stack) > 0:
                    stack_top = stack[-1]
                else:
                    stack_top = ''
            else:
                stack_top = s[index]
                stack.append(s[index])
                index+=1
        return "".join(stack)