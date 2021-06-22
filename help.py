import sys

sys.setrecursionlimit(10**9)

n = int(input())
arr = [int(x) for x in input().split(" ")]
N = len(arr)


def go(index, present):
    if index >= N:
        return 0
    if arr[index] > present:
        op1 = 1 + go(index+1, arr[index])
        op2 = go(index+1, present)
        return max(op1, op2)
    else:
        return go(index+1, present)


print(go(1, arr[0])+1)
