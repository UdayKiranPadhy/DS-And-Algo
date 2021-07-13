"""

Date :- 11/07/2021
Source :- 

1930. Unique Length-3 Palindromic Subsequences
Medium

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 10^5
s consists of only lowercase English letters.

"""


# My Approach
import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        strings = set()
        for i in range(N):
            remaining = s[i+1:]
            index = remaining.rfind(s[i])
            if index == -1:
                continue
            else:
                for j in range(i+1, i+index+1):
                    strings.add(s[i] + s[j] + s[i+index+1])
        return len(strings)


# Correct Solution
#
# Explanation
""" 
For each palindromes in format of "aba",
we enumerate the character on two side.

We find its first occurrence and its last occurrence,
all the characters in the middle are the candidate for the midd char.


Complexity
Time O(26n)
Space O(26)
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        res = 0
        for c in string.ascii_lowercase:
            i = s.find(c)
            j = s.rfind(c)
            if i > -1:
                res += len(list(set(s[i+1:j])))
        return res
