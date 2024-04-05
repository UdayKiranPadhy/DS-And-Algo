"""
https://leetcode.com/problems/palindrome-partitioning-ii/
Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition 
is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1
 

Constraints:
1 <= s.length <= 2000
s consists of lower-case English letters only.

"""

from functools import lru_cache


class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        palin_length = [[1] for i in range(N)]

        # Count Odd Length Palindromes
        for i in range(N):
            low = i - 1
            high = i + 1
            length = 1
            while low >= 0 and high < N and s[low] == s[high]:
                low -= 1
                high += 1
                length += 2
                if low + 1 >= 0:
                    palin_length[low + 1].append(length)

        # Count Even Palindromes
        for i in range(N - 1):
            low = i
            high = i + 1
            length = 0
            while low >= 0 and high < N and s[low] == s[high]:
                low -= 1
                high += 1
                length += 2
                if low + 1 >= 0:
                    palin_length[low + 1].append(length)

        print(s)
        print(palin_length)

        @lru_cache(None)
        def go(index, hop):
            if index >= N:
                return hop
            best = float('inf')
            for steps in palin_length[index]:
                best = min(best, go(index + steps, hop + 1))
            return best

        gg = go(0, 0)
        return gg - 1


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l + 1, r - 1)

        @lru_cache(None)
        def dp(i):  # s[i..n-1]
            if i == n:
                return 0
            ans = float('inf')
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    ans = min(ans, dp(j + 1) + 1)
            return ans

        return dp(0) - 1