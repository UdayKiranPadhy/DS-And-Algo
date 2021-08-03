"""
Source :- https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_length = 1
        max_palin = s[0]
        N = len(s)

        for i in range(N):
            low = i - 1
            high = i + 1
            length = 1
            # Count all the odd length Palindromes
            while (low >= 0 and high < N and s[low] == s[high]):
                length += 2
                if length > max_length:
                    max_length = length
                    max_palin = s[low:high+1]
                low -= 1
                high += 1

            # Count all the even length Palindromes
            low = i
            high = i+1
            length = 0
            while(low >= 0 and high < N and s[low] == s[high]):
                length += 2
                if length > max_length:
                    max_length = length
                    max_palin = s[low:high+1]
                low -= 1
                high += 1
        return max_palin
