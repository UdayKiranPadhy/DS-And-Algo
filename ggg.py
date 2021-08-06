n = int(input())

for row in range(n + 1):
    for space in range(n - row):
        print(" ", end="")
    for alpha in range(n, n - row, -1):
        print(chr(ord('`') + alpha), end="")
    for alpha in range(n - row + 1, n):
        print(chr(ord('`') + alpha + 1), end="")
    print()

for row in range(1, n):
    for space in range(row):
        print(" ", end="")
    for alpha in range(n, row, -1):
        print(chr(ord('`') + alpha), end="")
    for alpha in range(row, n - 1):
        print(chr(ord('`') + alpha + 2), end="")
    print()