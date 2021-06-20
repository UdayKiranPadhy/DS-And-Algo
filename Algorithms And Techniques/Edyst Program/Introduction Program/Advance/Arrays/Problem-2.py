def isqrt(n):
    """
    Return the integer part of the square root of the input.
    """
    if n < 0:
        raise ValueError("isqrt() argument must be nonnegative")
    if n == 0:
        return 0
    c = (n.bit_length() - 1) // 2
    # print(n.bit_length())
    a = 1
    d = 0
    for s in reversed(range(c.bit_length())):
        # Loop invariant: (a-1)**2 < (n >> 2*(c - d)) < (a+1)**2
        e = d
        d = c >> s
        print(a << d - e - 1)
        print(n >> 2 * c - e - d + 1)
        a = (a << d - e - 1) + (n >> 2 * c - e - d + 1) // a
    return a - (a * a > n)


a = 10
b = 12
print(a << b)
print(isqrt(12))