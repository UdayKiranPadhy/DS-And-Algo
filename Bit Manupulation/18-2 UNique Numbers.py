# Write a programe to find 2 unique numbers in a array where all
# the numbers are present twice except two unique numbers.

"""
Example is {2,4,6,7,4,5,6,2}

After finding xor of all the numbers we will get xor of 7 and 5
remaining all will cancel each other except 7 and 5

0111
0101
----
0010
----

Now we have to take xor of all numbers whose corresponding set bit matches 
with one.
0010  0100  0110  0111  0100  0101  0110  0010
2     4     6     7     4     5     6     2

as we got set bit at position 1 now take xor of all the bits which have set
in position 1
i.e 2 6 7 6 2

taking xor of this will leave out 7 which is one unique number

taking xor of 7 and the older xor value we will get 5
"""


def getbit(num: int, pos: int) -> int:
    return num & (1 << pos)


def unique(arr: list) -> int:
    xor = 0
    for i in arr:
        xor = xor ^ i
    gg = xor

    setbit = 0
    pos = 0
    while not setbit:
        setbit = xor & 1
        pos += 1
        xor = xor >> 1

    pos -= 1

    newxor = 0
    for i in arr:
        if getbit(i, pos):
            newxor = newxor ^ i

    second_num = gg ^ newxor
    return newxor, second_num


print(unique([2, 4, 6, 7, 4, 5, 6, 2]))
