"""
Date:- 3/07/21
Source Leetcode
https://leetcode.com/problems/gray-code/

89. Gray Code
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]
 

Constraints:

1 <= n <= 16

"""


# Gave TLE
class Solution:
    def grayCode(self, n: int) -> list[int]:
        elements = set()
        stack = [0]
        Solutions = []
        for i in range(1, 2**n):
            elements.add(i)

        def CanBeNext(prev, current):
            xor_gg = prev ^ current
            string = bin(xor_gg)[2:]
            if string.count('1') == 1:
                return True
            else:
                False

        def backtrack():
            if elements == set():
                Solutions.append(stack)
                return True
            for i in elements:
                if i in elements:
                    if CanBeNext(stack[-1], i):
                        stack.append(i)
                        elements.remove(i)
                        if backtrack():
                            return True
                        stack.pop()
                        elements.add(i)
            return False

        backtrack()
        return Solutions[0]


# Accepted Once
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        t = self.grayCode(n-1)
        return t + [i+(1 << (n-1)) for i in t][::-1]


n = int(input())

model = Solution()
print(model.grayCode(n))
