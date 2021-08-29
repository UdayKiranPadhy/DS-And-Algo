"""

Divide Two Integers
Medium

2102

7672

Add to List

Share
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""

# https://leetcode.com/problems/divide-two-integers

# I do not really like these type of problems, where you restricted in using
# operations. What we can use if we can not use multiplications and divisions:
# we can use only addition and subtraction. Let consider an example: 100 // 7

# We can try just to subtract 7 while it is possible. However potentially it
# can be quite long, if dividend is big and divisor is small. Let us multiply
# 7 by 2 (in fact it is not multiplication, but addition with itself), until
# we are smaller than 100. 7 -> 14 -> 28 -> 56. Ans subtract 56 now, so we
# have 8 as result and we need to divide 44 by 7 now. Repeat procedure, so
# we subtract 28, and we have 8 + 4 as result and 44 - 28 = 16 = 2. Finally,
# we subtract 14 and we have 8 + 4 + 2 = 14 as result.

# Let us precalculate pairs (7, 1), (14, 2), (28, 4), (56, 8). Then we iterate
# through these pairs in opposite direction and if we can subtract corresponding
# number, we subtract, if not - we go to the next one. Also we need to deal with
# signs and overflows here.

# Complexity: time complexity is O(log n), where n = divident/divisor: there
# will be O(log n) terms in our cand list as well as this is limit for number
# of steps. Space complexity is O(log n) as well. What I mean by honest here,
# that a lot of people here in discussion either use some tricks which are not
# allowed, or complexity is wrong.


class Solution:
    def divide(self, dividend, divisor):
        if dividend == -1 << 31 and divisor == -1:
            return (1 << 31)-1

        a, b = abs(dividend), abs(divisor)
        sign = (dividend < 0) == (divisor < 0)
        res, cand = 0, [(1, b)]

        while b << 1 <= a:
            cand += [(cand[-1][0] << 1, b << 1)]
            b <<= 1

        for pw, num in cand[::-1]:
            if a >= num:
                a, res = a - num, res + pw

        return res if sign else -res
