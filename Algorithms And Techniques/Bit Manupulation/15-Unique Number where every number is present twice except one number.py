# Program to find unique Number where every number is present twice except one number
"""
We have noticed that if X has 1 in that position, we will have odd number 
of 1s in that position.

If X has 0 in that position, we will have odd number of 0 in that position.

If you look at the bit operators, XOR is exactly what we need.

XOR will return 1 only on two different bits. So if two numbers are the same, 
XOR will return 0.

Finally, there is only one number left.

A ^ A = 0 and A ^ B ^ A = B.

So, all even occurences will cancel out using XOR.
"""
class Solution:
    def singleNumber(self, A):
        xor=A[0]
        for i in range(1,len(A)):
            xor=xor^A[i]
        return xor