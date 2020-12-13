"""
Check weather a given number is a power of 2
"""
# Approch 1
"""
Divide the number by 2 continuesly until we get 1
"""
# Approch 2
"""
Bit manupalation
"""
"""
We know that n & n-1 will give 0 if n is power of 2
n = 6
    1 1 0

n - 1 = 5
        1 0 1
    we can see that n-1 give the number we get if we apply not on the number's left to 
    we get all 0's
"""

def ispower2(n):
    if n == 0:
        return 1
    return 1 if (n & (n - 1)) == 0 else 0

print(ispower2(8))
