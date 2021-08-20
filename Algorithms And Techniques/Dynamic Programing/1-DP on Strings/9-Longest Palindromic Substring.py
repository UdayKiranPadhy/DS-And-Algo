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


"""
Let us look at possible places of middle of our palindrome and expand to the left 
and to the right until we either reached on of the ends of symbols are not equal. 
Also, because we need to return not only length of longest palindromic substring, 
but substring itself, our helper function will return this string.

Note also, that there are two different type of palindromes:

With odd length, we use helper(k, k) for them.
With even length, we use helper(k, k+1) for them.
Complexity There will be 2n - 1 possible centers and O(n) comparison for each of 
them, so final time complexity is O(n^2). Space complexity is O(n)

Further discussion there is also classical dynamic programming for this problem 
with also O(n^2) complexity, however in practice it can work much slower if we do 
not do optimiaztions: reason that it will be indeed n^2 operations, whereas on our 
approach here we do a lot of early stoppings. There is also ofcourse Manacher’s 
algorithm with complexity O(n), which sometimes useful for competitions, and you 
should have code avaliable somewhere, but which is in my opitions out of scope 
for middle difficulty problem.

"""


class Solution:
    def longestPalindrome(self, s):
        n, ans = len(s), ""

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1:j]

        for k in range(n):
            ans = max(helper(k, k), helper(k, k + 1), ans, key=len)
        return ans
