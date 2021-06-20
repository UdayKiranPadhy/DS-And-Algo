# Transpose of a matrix (all langs)

"""
Write a program to find the transpose of a given n*m matrix.

Input Format:
First line take an Integer from stdin  which is number of rows n.
Second line take an Integer from stdin which is number of columns m.
Third line take an Integers which are matrix elements
Output Format:

Transpose of a matrix

Example Input:

1   2   3
4   5   6
7   8   9


Output:

1   4   7
2   5   8
3   6   9

"""


m = 3
n = 3
s = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
list2 = []
start = 0
for i in range(m):
    end = start + n
    list2.append(s[start:end])
    start = end
list2 = s
result = []
result.extend(list2)
print(result)
print(list2)

for i in range(m):
    for j in range(n):
        # print(i, j)
        result[j][i] = list2[i][j]
for r in result:
    print(r)
print()
for r in list2:
    print(r)