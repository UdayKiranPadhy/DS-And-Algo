"""


https://leetcode.com/problems/count-numbers-with-unique-digits/description/

357. Count Numbers with Unique Digits

Medium

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.



Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1


Constraints:

0 <= n <= 8

"""

# the tight variable is used to count number like 0031 , 0002 since as you can see we are repeating 0 hear many times

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dfs(mask,k,tight):
            if k == 0:
                return 1
            total = 0
            for i in range(10):
                if i== 0 and tight:
                    total += dfs(mask,k-1,True)
                elif mask & (1<<i) == 0:
                    total += dfs(mask | (1<<i), k-1,False)
            return total
        return dfs(0,n,True)
