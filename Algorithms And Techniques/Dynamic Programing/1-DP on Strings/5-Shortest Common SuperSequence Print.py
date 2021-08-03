"""

1092. Shortest Common Supersequence
Hard

Given two strings str1 and str2, return the shortest string that has both 
str1 and str2 as subsequences.  If multiple answers exist, you may 
return any of them.

(A string S is a subsequence of string T if deleting some number of 
characters from T (possibly 0, and the characters are chosen 
anywhere from T) results in the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

"""


# Consider the strings "abcf" and "bdcf". They share the characters 'b', 'c' and 'f'.
# The first string has the character 'a' appearing before the subsequence "bcf",
# and the second has the character 'd'
# appearing before the subsequence "cf".
# Thus, the SCS would be "abdcf" with length 5, that contains all the characters
# from both strings, and preserves the
# relative ordering of the characters.

# It follows from the above that in order to find the SCS, we first need to
# find the longest common subsequence (LCS)
# between the two strings. Having found the LCS, we compare each character
# in the input strings with a character
# in the LCS; let's call these characters 'x', 'y' and 'z', respectively.
# If all three characters are the same,
# then we found a character from the LCS, and it is appended to the SCS.
# If only one of 'x' and 'y' is the same as 'z',
# then we append the character that is NOT equal to the SCS (like 'a' and
# 'd' in the example above). If none of 'x' or
# 'y' is equal to 'z', both are appended to the SCS. At the end, we append
# the remaining characters from the strings
# to the SCS.

# Note that if only the length of the SCS is required, we don't need to
# reconstruct the SCS, the length is simply
# given by len(s1) + len(s2) - len(LCS).


from collections import deque


class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:

        def longest_common_subsequence(s1: str, s2: str) -> str:
            # dp[i][j] is the length of the longest common subsequence of s1[:i] and s2[:j]
            dp: list[list[int]] = [[0] * (len(s2) + 1)
                                   for _ in range(len(s1) + 1)]

            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            i = len(s1)
            j = len(s2)
            lcs = deque()
            while i > 0 and j > 0:
                if s1[i - 1] == s2[j - 1]:
                    i -= 1
                    j -= 1
                    lcs.appendleft(s1[i])
                elif dp[i][j] == dp[i - 1][j]:
                    i -= 1
                else:
                    j -= 1

            return "".join(lcs)

        lcs = longest_common_subsequence(s1, s2)

        i = j = k = 0
        scs = []
        while i < len(s1) and j < len(s2) and k < len(lcs):
            if s1[i] == s2[j] == lcs[k]:
                scs.append(lcs[k])
                i += 1
                j += 1
                k += 1
            elif (s1[i] == lcs[k]) and (s2[j] != lcs[k]):
                scs.append(s2[j])
                j += 1
            elif (s1[i] != lcs[k]) and (s2[j] == lcs[k]):
                scs.append(s1[i])
                i += 1
            else:
                scs.append(s1[i])
                scs.append(s2[j])
                i += 1
                j += 1

        while i < len(s1):
            scs.append(s1[i])
            i += 1
        while j < len(s2):
            scs.append(s2[j])
            j += 1

        gg = "".join(scs)
        return gg
