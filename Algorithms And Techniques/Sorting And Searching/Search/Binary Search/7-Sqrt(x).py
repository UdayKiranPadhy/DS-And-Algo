"""

69. Sqrt(x)
Easy

2521

2629

Add to List

Share
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1

"""


class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        low = 1
        high = x // 2 + 1

        while low < high:

            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            if square > x:
                high = mid
            else:
                low = mid + 1

        return low - 1
