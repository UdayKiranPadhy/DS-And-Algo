# Set the bit at the given position
# n=0101
# set the bit at position 4
# n=1101


# Left shift 1 i time and apply OR operatation
def setBit(n, i):
    return n | (1 << i - 1)


print(setBit(5, 4))