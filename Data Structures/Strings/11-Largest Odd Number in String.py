"""
Link :- https://leetcode.com/problems/largest-odd-number-in-string/
Date :- 20/06/2021

1903. Largest Odd Number in String
Easy

42

5

Add to List

Share
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
 

Constraints:

1 <= num.length <= 10^5
num only consists of digits and does not contain any leading zeros.


"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) -1
        while i >= 0 and int(num[i])%2 == 0:
            i-=1
        return num[:i+1]