"""
Shortest Common Supersequence
Given two strings str1 and str2, the task is to find the length of the shortest 
string that has both str1 and str2 as subsequences.

Examples : 

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.
"""

# Solution
# This problem is closely related to longest common subsequence problem. Below are steps.
# 1) Find Longest Common Subsequence (lcs) of two given strings.
# For example, lcs of “geek” and “eke” is “ek”.
# 2) Insert non-lcs characters (in their original order in strings) to the lcs found above,
# and return the result. So “ek” becomes “geeke” which is shortest common supersequence.
# Let us consider another example, str1 = “AGGTAB” and str2 = “GXTXAYB”.
# LCS of str1 and str2 is “GTAB”. Once we find LCS, we insert characters of both strings in
# order and we get “AGXGTXAYB”
# How does this work?
# We need to find a string that has both strings as subsequences and is shortest such string.
# If both strings have all characters different, then result is sum of lengths of two given
# strings. If there are common characters, then we don’t want them multiple times as the task
# is to minimize length. Therefore, we fist find the longest common subsequence,
# take one occurrence of this subsequence and add extra characters.

# Length of the shortest supersequence
# = (Sum of lengths of given two strings)
# - (Length of LCS of two given strings)


def SCSS(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[-1][-1]

    return m + n - lcs


X = "AGGTAB"
Y = "GXTXAYB"
print(SCSS(X, Y))
