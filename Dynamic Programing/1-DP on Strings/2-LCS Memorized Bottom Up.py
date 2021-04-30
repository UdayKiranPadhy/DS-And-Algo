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

# Memorizatation version is same as just Recursive Calls + A table to stor the values
# in Top to down Approach we only use table and no recursive Calls

# Lets just modify the code of previous Problem
def LCS(string1: str, string2: str, m: int, n: int) -> int:
    global dp
    if m == 0 or n == 0:
        dp[m][n]
        return 0
    if dp[m][n] == -1:
        if string1[m - 1] == string2[n - 1]:
            dp[m][n] = 1 + LCS(string1, string2, m - 1, n - 1)
            return dp[m][n]

        else:
            dp[m][n] = max(
                LCS(string1, string2, m - 1, n), LCS(string1, string2, m, n - 1)
            )
            return dp[m][n]
    else:
        return dp[m][n]


string1 = "GGGg"
string2 = "GGGG"
n = len(string2)
m = len(string1)
dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
print(LCS(string1, string2, m, n))
# print(dp)


    def lcs(self,m,n,s1,s2):
        dp = [[0 for _ in range(n+1)]for __ in range(m+1)]
        for j in range(1,m+1):
            for i in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[m][n] = 1+dp[m-1][n-1]
                else:
                    dp[m][n] = max(dp[m-1][n],dp[m][n-1])
        
        return dp[-1][-1]