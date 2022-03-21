"""

22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""


# Problem statement
# https://leetcode.com/problems/generate-parentheses/

# Solution
# At any instant of moment we would be checking weather we can place a closing
# bracket and a opening bracket , if we can then place it and increase the
# length of the string and run it till it becomes 2*n length string.

# In order to tell weather we can place a bracket we can use logic of minimum
# swaps required to make balanced brackets (array).

class Solution:
    def generateParenthesis(self, n):

        ans = []

        def backtrack(length, brackets, current):
            if length == 2*n and brackets == 0:
                ans.append(current[:])
                return
            if length == 2*n and brackets != 0:
                return

            if brackets + 1 <= n:
                backtrack(length + 1, brackets+1, current+"(")
            if brackets - 1 >= 0:
                backtrack(length+1, brackets - 1, current+")")

        backtrack(0, 0, "")
        return ans


model = Solution()

print(model.generateParenthesis(1))
print(model.generateParenthesis(3))

# Solution 2
# For each valid parentheses there smallest k, for which the first k symbols
# compose well-formed parentheses: (left)right. Let us ans[i] be all valid
# parentheses of length i. Then we can generate them using recursion. For
# every k in range(n+1) and for every i in range(k) we choose left part and
# right part and append it to final answer. Because we memorize our intermediate
# results, we can also say that we use dp approach here.

# Complexity
# Time complexity is O(C_n * n) = O(4^n/n^0.5), where C_n is Catalan number.
# Space complexity is the same.


class Solution:
    def generateParenthesis(self, n):
        ans = [[] for _ in range(n+1)]
        ans[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                for left in ans[i]:
                    for right in ans[k-i-1]:
                        ans[k].append("(" + left + ")" + right)

        return ans[-1]
