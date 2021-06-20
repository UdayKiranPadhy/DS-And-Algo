# Update i’th bit to the given value
"""
Mask: mask has all the bits set to one except ith bit.

n = n & mask, ith bit is cleared.
Now, to set ith bit to value, we take value << pos as the mask

n=0101
Suppose we need to update bit at position i=1 to 1
1<<i
0010
~0010 = 1101
0101 & 1101
0101

Now apply set bit 
1 << i
0101 | 0010
0111
"""
