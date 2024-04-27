"""

URL: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 
Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

 
Constraints:

	1 <= words.length <= 105
	words[i].length == 2
	words[i] consists of lowercase English letters.

"""
from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = Counter(words)
        ans = 0

        # Handeling non equal elements
        for word, freq in word_dict.items():
            if word == word[::-1]:
                continue
            reverse = word[::-1]
            if reverse not in word_dict:
                continue
            pairs = min(freq, word_dict[reverse])
            word_dict[word] -= pairs
            word_dict[reverse] -= pairs
            ans += 4 * pairs

        # Handeling equal elements
        odd = 0
        for word, freq in word_dict.items():
            if word != word[::-1]:
                continue
            if freq % 2 == 1:
                odd = 1
            ans += 4 * (freq // 2)
        if odd:
            ans += 2
        return ans