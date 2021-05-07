"""
We define d(X, Y) as number of different corresponding bits in binary 
representation of X and Y. For example, d(3, 9) = 2, since binary 
representation of 3 and 9 are 0011 and 1001, respectively. 
The first and the third bit differ, so f(3, 9) = 2.

You are given an array of N positive integers, A1, A2 ,…, AN. 
Find sum of d(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. 
Return the answer modulo 10^9+7.

For example,
A= [3,7,9]
We return
  d(3,3) + d(3,7) + d(3,9)
+ d(7,3) + d(7,7) + d(7,9)
+ d(9,3) + d(9,7) + d(9,9)    

  0 + 1 + 2
+ 1 + 0 + 3
+ 2 + 3 + 0
= 12
Thus, we return 12
"""


def D(num1, num2):
    return bin(num1 ^ num2).count("1")


class Solution:
    def cntBits(self, A):
        sum = 0
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                sum += D(A[i], A[j])
        return sum


# Method 2 :
"""
Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.
Lets say A = count of elements which are 0
and B = count of elements which are 1

In this case our answer is just 2AB, since each such pair contributes 
1 to answer.

Can you combine this logic if we have multiple bits?

Note that all bits are independent in counting, since we are counting 
number of bits which are different in each pair.
So, we just do the same process for all different bits. Since Ai is 
an integer, we just have to do this for 31 different bits, so our 
solution is O(31*N).
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        l = len(A)
        ans = 0
        for i in range(31):
            count1 = 0
            for a in A:
                if a & (1 << i) > 0:
                    count1 += 1
            ans += 2 * count1 * (l - count1)
        return ans % 1000000007


# Solution 2
import numpy as np


class Solution:
    # @param A : integer
    # @return an integer
    def cntBits(self, A):
        l = np.array(A, dtype=np.uint32).reshape(-1, 1)
        l = np.unpackbits(l.view(np.uint8), axis=1)
        ans = np.count_nonzero(l == 0, axis=0) * np.count_nonzero(l == 1, axis=0)
        return int(2 * ans.sum()) % (10 ** 9 + 7)
