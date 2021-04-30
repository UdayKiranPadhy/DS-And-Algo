"""
Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""

word = "abc"
# word="aaa"

m = len(word)

dp = [[0 for _ in range(m)] for __ in range(m)]

count = 0
for i in range(m):
    count += 1
    dp[i][i] = 1

for i in range(1,m):
    for j in range(i):
        if 
#    a  a  a
# a  1  0  0
# a  0  1  0
# a  0  0  1

# for i in range(1, m):
#     for j in range(0, i):
#         dp[i][j] = "uday"
# print(dp)
