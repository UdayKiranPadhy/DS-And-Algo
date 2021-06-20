def subsets(l, n):
    for i in range(1 << n):
        for j in range(n):
            if i & 1 << j:
                print(l[j], end=" ")
        print()


print(subsets([1, 2, 3, 4], 4))

"""
000  {}
001  {c}
010  {b}
011  {b, c}
100  {a}
101  {a, c}
110  {a, b}
111  {a, b, c}
"""