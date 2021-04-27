"""
Find XOR of numbers from the range [L, R]
Given two integers L and R, the task is to find the XOR of elements of the range [L, R]. 
Examples :‘ 
 

Input: L = 4, R = 8 
Output: 8 
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
Input: L = 3, R = 7 
Output: 3 
"""

from operator import xor


def findXOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    else:
        return 0


def findXORFunction(l, r):
    return xor(findXOR(l - 1), findXOR(r))


print(findXORFunction(4, 8))


"""
Using this approach, we have to find xor of elements from the range [1, L – 1] 
and from the range [1, R] and then xor the respective answers again to get 
the xor of the elements from the range [L, R]. This is because every 
0element from the range [1, L – 1] will get XORed twice in the result 
resulting in a 0 which when XORed with the elements of the range [L, R] 
will give the result.
"""