"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
5754. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of 
length three in s​​​​​​.

Note that if there are multiple occurrences of the same 
substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", 
"bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.

"""


class Solution:

    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        def goodstring(l1):
            for i in range(2):
                if l1[i] in l1[:i] + l1[i+1:]:
                    return False
            else:
                return True
        count = 0
        stack = list(s[:3])
        if goodstring(stack):
            count += 1
        for i in range(3, len(s)):
            stack.pop(0)
            stack.append(s[i])
            if goodstring(stack):
                count += 1
        return count


model = Solution()
print(model.countGoodSubstrings("aababcabc"))


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        return sum(s[i] != s[i-1] != s[i-2] != s[i] for i in range(2, len(s)))


class Solution():
    def countGoodSubStrings(self, s: str):
        count = 0
        for x, y, z in zip(s, s[1:], s[2:]):
            if x != y and y != z and z != x:
                count += 1
        return count
