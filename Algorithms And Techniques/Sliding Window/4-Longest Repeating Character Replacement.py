"""

https://leetcode.com/problems/longest-repeating-character-replacement/


424. Longest Repeating Character Replacement
Medium

10288

484

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        window = defaultdict(lambda: 0)
        left = 0
        max_length = -1

        for right in range(N):
            window[s[right]] += 1
            max_freq = max(window.values())
            if right - left + 1 - max_freq > k:
                while left <= right and right - left + 1 - max_freq > k:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                    max_freq = max(window.values())
            max_length = max(max_length, right - left + 1)
        return max_length


model = Solution()
print(model.characterReplacement("AABABBA", 1))
