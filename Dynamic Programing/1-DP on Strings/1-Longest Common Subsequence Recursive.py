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

# This is a recurssive approach
def LCS(string1: str, string2: str, m: int, n: int) -> int:
    if m == 0:
        return 0
    elif n == 0:
        return 0
    elif string1[m - 1] == string2[n - 1]:
        return 1 + LCS(string1, string2, m - 1, n - 1)
    else:
        return max(LCS(string1, string2, m - 1, n), LCS(string1, string2, m, n - 1))


print(LCS("UDAY", "AJAY", 4, 4))
