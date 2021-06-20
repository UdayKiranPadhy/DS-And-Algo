"""
LCS Problem Statement: 

For Reference
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

For Practice:
https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1

Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.


Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Longest Common Subsequence 
Given two sequences, find the length of longest subsequence present in both of them. 
Both the strings are of uppercase.

Example 1:

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
Example 2:

Input:
A = 3, B = 2
str1 = ABC
str2 = AC
Output: 2
Explanation: LCS of "ABC" and "AC" is
"AC" of length 2.
Your Task:
Complete the function lcs() which takes the length of two strings respectively and two strings as input parameters and returns the length of the longest subsequence present in both of them.

Expected Time Complexity : O(|str1|*|str2|)
Expected Auxiliary Space: O(|str1|*|str2|)

Constraints:
1<=size(str1),size(str2)<=103

Topic Tags
 Dynamic Programming
"""


# Geeks For Geeks Solution
# First try to solve the question recursively.
# Now, Let’s define the state of DP.
# There are 2 states for this DP. String 1 and String 2, as any combination of
# characters of these strings can form subsequence, hence we need to iterate every
# character of string 2 for every character of string 1

# Therefore, a 2D DP array will be formed.

# Complete Solution:

# A character may or may not be included in the subsequence. There are 2 cases:
# If character of string1 and string2 match, then it may be a part of subsequence.
# If not, then 2 more cases arise:
# Either the matching character appears in string1 before the position of this character
# Or matching character appears in string2 before the position of character
# Therefore,
# if character match then DP[i][j] = DP[i-1][j-1] + 1
# else DP[i][j] = max(DP[i-1][j], DP[i][j-1])
# Iterate for complete DP array
# Return DP[m][n] (m, n - size of strings)


def LCS(string1, string2):
    m = len(string1)
    n = len(string2)

    dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[-1][-1]


print(LCS("Uday", "Ajay"))
