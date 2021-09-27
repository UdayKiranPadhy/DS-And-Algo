"""

49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

# Problem statement
# https://leetcode.com/problems/group-anagrams/

# Solution 1
# First idea is to notice that if we have two anagrams, than when we sort
# symbols in each of them, then we will have exactly the same string. So
# we need for each string to sort it and then use defaultdict.

# Complexity
# Time complexity will be O(nk * log k), space complexity is O(nk).

# Code

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        t = defaultdict(list)
        for s in strs:
            t["".join(sorted(s))].append(s)
        return t.values()
# Solution 2
# Two strings are anagrams if and only if their character counts, that is
# frequencies of each letter a, b, ..., z are the same. So it can be done
# with defauldict(list), where key is 26-element list and values are strings,
# corresponding to this key.

# Complexity
# Time complexity is O(nk + 26n), where n is number of strings and k is the
# length of the biggest string. Space complexity is O(26n).

# Code


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
