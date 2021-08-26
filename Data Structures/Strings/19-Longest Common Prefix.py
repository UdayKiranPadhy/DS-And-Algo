"""


14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Calculate the minimum length string from the strs
        min_length = 10**6
        for i in strs:
            min_length = min(min_length, len(i))

        length = 0
        comefrombreak = False
        for i in range(min_length):
            to_find = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == to_find:
                    continue
                else:
                    comefrombreak = True
                    break
            if comefrombreak:
                break
            else:
                length += 1
        return strs[0][:length]
