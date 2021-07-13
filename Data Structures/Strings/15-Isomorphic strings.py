"""
Source :- https://leetcode.com/problems/isomorphic-strings/solution/
Date :- 13/07/21

205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character 
may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


"""

# My Trails :


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alpha1 = {}
        for i in s:
            if i in alpha1:
                alpha1[i] += 1
            else:
                alpha1[i] = 1

        alpha2 = {}
        for i in t:
            if i in alpha2:
                alpha2[i] += 1
            else:
                alpha2[i] = 1
        value1 = sorted(alpha1.values())
        value2 = sorted(alpha2.values())
        if value1 == value2:
            return True
        return False


# Fails For test cases like bbbaaaba , aaabbbba


# Correct Solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i, j in zip(s, t):
            if i in dict1 and dict1[i] != j:
                return False
            if j in dict2 and dict2[j] != i:
                return False
            else:
                dict1[i] = j
                dict2[j] = i
        return True

# Correct Solution


class Solution:

    def transformString(self, s: str) -> str:

        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):

            if c not in index_mapping:
                index_mapping[c] = i

            new_str.append(str(index_mapping[c]))

        return "".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
