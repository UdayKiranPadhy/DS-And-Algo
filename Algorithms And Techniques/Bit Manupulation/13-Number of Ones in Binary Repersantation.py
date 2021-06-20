"""
(n & n-1) has same bits as n except the rightmost set bit
n = 19 = (01011)2       n = 18 = (01010)2           n = 16 = (01000)2
n-1 = 18 = (01010)2     n-1 = 17 = (01001)2         n-1 = 15 = (00111)2

n=n & n-1               n = n & n-1                 n = n & n-1
 = 01011 & 01010        = 01010 & 01001               = 01000 & 00111
 = 01010 = (18)10       = 01000 = (16)10               = 00000 = (0)10
"""

def count1s(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count


# print(count1s(7))