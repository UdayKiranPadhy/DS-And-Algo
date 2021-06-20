"""
Single Number v2
Given an array of integers, every element appears thrice except for one 
which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Can you implement it without using extra memory?

Input : [7, 0, 10, 3, 3, 0, 0, 3, 7, 7]
Output : 10

"""

# True Solution
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        n = len(A)

        for i in range(0, 32):

            sm = 0
            x = 1 << i
            for j in range(0, n):
                if A[j] & x:
                    sm += 1
            if sm % 3:
                res = res | x
        return res


# My Solution
def unique(arr: list) -> int:
    bits = [0] * 32  # Considering Size of int as 2^32 - 1
    for i in arr:
        temp = bin(i).lstrip("0b").rjust(32, "0")
        for i in range(len(temp)):
            if temp[i] == "1":
                bits[i] += 1
    for i in range(len(bits)):
        bits[i] = bits[i] % 3
        bits[i] = str(bits[i])
    string = "".join(bits)
    return int(string, 2)


print(unique([1, 3, 2, 3, 4, 2, 1, 1, 3, 2]))
