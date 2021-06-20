# n=0101  (5)
# Suppose we need to get bit at position ,i=2
# We have to tell weather the bit is 0 or 1 in the given position of that bit

# make a number where we have one only at that position where we need to find
# the bit
# print(bin(1<<2).lstrip('0b'))
# 100


# and after that we will apply and operator to this number and the given number 'n'
# what happens in and is we will only get the bit where we have kept one
# remaining all are zero's

# So the procedure is something like this
# if n &(1<<i)!=0 then bit is 1 else the bit is zero


def getBit(n, i):
    return 1 if (n & (1 << i - 1) != 0) else 0


print(getBit(5, 3))

# 2nd method
# Mask: Right shift n ‘i’ times, and check the first bit.
def getBit2(n, i):
    return (n >> i - 1) & 1


print((getBit2(5, 3)))