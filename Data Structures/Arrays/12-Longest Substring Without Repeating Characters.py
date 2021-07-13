"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring 
without repeating characters.
 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a 
subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# Solution
"""
This is classical problem for sliding window. Let us keep window with 
elements [beg: end), where first element is included and last one is not. 
For example [0, 0) is empty window, and [2, 4) is window with 2 elements: 2 
and 3. Let us discuss our algorithm now:

window is set of symbols in our window, we use set to check in O(1) if new symbol 
inside it or not.
beg = end = 0 in the beginning, so we start with empty window, also ans = 0 and n = len(s).
Now, we continue, until one of two of our pointers reaches the end. First, we 
try to extend our window to the right: check s[end] in window and if we can, add 
it to set, move end pointer to the right and update ans. If we can not add new symbol 
to set, it means it is already in window set, and we need to move left pointer and 
move beg pointer to the right.

Complexity
We move both of our pointers only to the left, so time complexity is O(n). Space complexity is O(1).
"""

# Approach - 1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = maxCount = 0
        seen = []

        for x in s:
            if x not in seen:
                seen.append(x)
                count = len(seen)
                if count > maxCount:
                    maxCount = count
            else:
                seen[:seen.index(x)+1] = []
                seen.append(x)
                count = 0
        return maxCount


# Approach - 2
class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()
        beg, end, ans, n = 0, 0, 0, len(s)

        while beg < n and end < n:
            if s[end] not in window:
                if end + 1 < n:
                    window.add(s[end])
                end += 1
                ans = max(ans, end - beg)
            else:
                window.remove(s[beg])
                beg += 1

        return ans
