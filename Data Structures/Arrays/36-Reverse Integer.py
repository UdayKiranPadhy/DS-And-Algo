"""

Reverse Integer
Easy

5436

8141

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-2^31 <= x <= 2^31 - 1

"""

# Solution
"""
Be careful with border cases, in python you can go to string, invert, then go back.

Complexity
Complexity is O(logn), both time and space.
"""

# Code


class Solution:
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        s = sign * int(str(abs(x))[::-1])
        return 0 if s > 2**31 - 1 or s < -2**31 else s


# If this is not allowed, use idea of stack, where we divide number by 10 and put this as new digit to new number. Time and space complexity is also O(logn).

class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x, n = abs(x), 0

        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10

        return 0 if n > 0x7FFFFFFF else n*sign


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            gg = int('-'+x[::-1])
            return gg if gg > -(2**31) else 0
        gg = int(x[::-1])
        return gg if gg < (2**31)-1 else 0
