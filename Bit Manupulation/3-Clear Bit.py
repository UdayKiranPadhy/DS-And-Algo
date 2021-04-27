# Clear ith Bit of the given Number.
"""
n=0101
Suppose we need to clear the bit at the position i=3 
1<<i=0100
~0100 = 1011
now perform AND operator to the original number
1011 & 0101
0001

Mask: ~ (1 << i )
In the mask, all the bits would be one, except the ith bit. 
Taking bitwise AND with n
would clear the ith bit.

"""


n = 1 << 2
# print(n)
# 4 0100

# n = not n
# print(n) #False

n = ~n
# print(n)  # -5

# The problem with using ~ in Python, is that it works with signed integers.
# This is also the only way that really makes sense unless you limit yourself to a particular number of bits.
# It will work ok with bitwise math, but it can make it hard to interpret the intermediate results.

# So for not of a number we need to subtract the number with all one's number
# not of 1100 is
# 1111 - 1100
# 0011


def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


# Do it YourSelf stop coping every thing