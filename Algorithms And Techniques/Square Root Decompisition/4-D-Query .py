"""
Problem Statement :- https://www.spoj.com/problems/DQUERY/

Given a sequence of n numbers a1, a2, ..., an and a number of d-queries. 
A d-query is a pair (i, j) (1 ≤ i ≤ j ≤ n). For each d-query (i, j), you have to 
return the number of distinct elements in the subsequence ai, ai+1, ..., aj.

Input
Line 1: n (1 ≤ n ≤ 30000).
Line 2: n numbers a1, a2, ..., an (1 ≤ ai ≤ 106).
Line 3: q (1 ≤ q ≤ 200000), the number of d-queries.
In the next q lines, each line contains 2 numbers i, j representing a d-query (1 ≤ i ≤ j ≤ n).

Output
For each d-query (i, j), print the number of distinct elements in the subsequence 
ai, ai+1, ..., aj in a single line.
 

Example
Input
5
1 1 2 1 3
3
1 5
2 4
3 5

Output
3
2
3 

"""
import math
from functools import cmp_to_key

# Inputs
n = input()
arr = [int(x) for x in input().split()]
queries = []
for q in range(int(input())):
    l, r = input().split()
    queries.append((q, int(l), int(r)))

# Computation of root blocks
root = math.ceil(math.sqrt(len(arr)))


def compare(element1, element2):
    if element1[1]//root == element2[1]//root:
        return element1[2] - element2[2]
    return element1[1]//root - element2[1]//root


queries.sort(key=cmp_to_key(compare))

answer = [0]*len(queries)

curr_l = -1
curr_r = -1
curr_dist = 0
curr_set = {}

for q in queries:
    index, l, r = q
    while curr_l < l:
        curr_l += 1
        if arr[curr_l] in curr_set:
            curr_set[arr[curr_l]] += 1
        else:
            curr_dist += 1
            curr_set[arr[curr_l]] = 1

    while curr_r < r:
        curr_r += 1
        if arr[curr_r] in curr_set:
            curr_set[arr[curr_r]] += 1
        else:
            curr_dist += 1
            curr_set[arr[curr_r]] = 1
    while curr_l > l:
        curr_set[arr[curr_l]] -= 1
        if curr_set[arr[curr_l]] == 0:
            curr_dist -= 1
        curr_l -= 1
    while curr_r > r:
        curr_set[arr[curr_r]] -= 1
        if curr_set[arr[curr_r]] == 0:
            curr_dist -= 1
        curr_r -= 1
    answer[index] = curr_dist

for _ in answer:
    print(_)
