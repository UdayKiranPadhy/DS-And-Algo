"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Find the Index of the First Occurrence in a String

Implement strStr()
Easy

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

"""



# Problem statement
# https://leetcode.com/problems/implement-strstr/

# Solution
# We need to find if one string is substring of another, for this problem O(nk) solution 
# is enough, however there is KMP algorighm with O(n+k) complexity. Actually, function 
# in in python will give your in average the same complexity.

# Complexity
# Time is O(n+k), space is O(n+k) as well.

# Code
class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        else:
            return len(haystack.split(needle)[0])

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


# KMP Algo
# https://www.youtube.com/watch?v=qases-9gOpk&ab_channel=codestorywithMIK


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def buildLPS(needle: str) -> List:
            N = len(needle)
            lps = [0] * N
            j = 0
            for i in range(1, N):
                while needle[i] != needle[j] and j > 0:
                    j = lps[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                    lps[i] = j
            return lps

        lps = buildLPS(needle)
        i = j = 0
        N, M = len(haystack), len(needle)
        while i < N:
            while haystack[i] != needle[j] and j > 0:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
                if j == M:
                    return i - M + 1
            i += 1
        return -1
