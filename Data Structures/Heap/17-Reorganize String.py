"""

767. Reorganize String
Medium

4347

170

Add to List

Share
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

https://leetcode.com/problems/reorganize-string/

"""

# https://www.youtube.com/watch?v=2g_b1aYTHeg&ab_channel=NeetCode
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []

        frequency = Counter(s)

        for char, freq in frequency.items():
            heapq.heappush(max_heap, (-freq, char))

        result = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if result and result[-1] == char:
                if not max_heap:
                    return ""
                freq2, char2 = heapq.heappop(max_heap)
                result += char2
                if freq2 + 1 < 0:
                    heapq.heappush(max_heap, (freq2 + 1, char2))
                heapq.heappush(max_heap, (freq, char))
            else:
                result += char
                if freq + 1 < 0:
                    heapq.heappush(max_heap, (freq + 1, char))
        return result
