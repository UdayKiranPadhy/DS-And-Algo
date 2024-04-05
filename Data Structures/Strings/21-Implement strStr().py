"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
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