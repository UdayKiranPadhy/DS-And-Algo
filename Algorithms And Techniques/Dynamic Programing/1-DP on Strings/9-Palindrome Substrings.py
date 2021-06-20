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

# https://www.youtube.com/watch?v=EIf9zFqufbU&t=1s&ab_channel=AlexanderLe


def PS(string):
    m = len(string)
    dp = [[0] * m for i in range(m)]
    count = 0
    for i in range(m):
        count += 1
        dp[i][i] = 1

    for j in range(1, m):
        for i in range(0, j):
            if string[j] == string[i] and i + 1 == j:
                count += 1
                dp[i][j] = 1
            elif string[j] == string[i] and dp[i + 1][j - 1] == 1:
                dp[i][j] = 1
                count += 1
    print(dp)
    return count


print(PS("aabaaca"))
print(PS("aaa"))
