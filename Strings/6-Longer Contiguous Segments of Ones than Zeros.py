"""
Problem Statement: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

1869. Longer Contiguous Segments of Ones than Zeros
Easy
Given a binary string s, return true if the longest contiguous segment of 
1s is strictly longer than the longest contiguous segment of 0s in s. 
Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has 
length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is 
considered to have length 0. The same applies if there are no 1s.

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.

Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.


"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count_1 = 0
        count_0 = 0
        max_count1 = 0
        max_count0 = 0
        for i in s:
            if i == '1':
                count_0 = 0
                count_1 += 1
                if max_count1 < count_1:
                    max_count1 = count_1
            else:
                count_1 = 0
                count_0 += 1
                if max_count0 < count_0:
                    max_count0 = count_0
        if max_count1 > max_count0:
            return True
        else:
            return False


# Note u can also do using Sliding Window
