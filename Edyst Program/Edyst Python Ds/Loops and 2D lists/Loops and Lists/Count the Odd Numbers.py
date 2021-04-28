"""
Count the odd numbers
Complete the given function solve, which takes a list A as parameter, you have to return the number of odd numbers in the list.

Example Input:
10 18 73 50 32 61

Output:
2
"""


def solve(A):
    l=[]
    for i in range(len(A)):
        if A[i] % 2 == 0:
            continue
        else:
            l.append(A[i])
    return l


print(solve([1, 2, 3, 4, 5, 6]))
