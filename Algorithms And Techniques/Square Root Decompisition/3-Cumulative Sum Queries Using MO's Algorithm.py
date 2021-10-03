"""
Problem Statement :- https://www.spoj.com/problems/CSUMQ/

William Macfarlane wants to look at an array.

You are given a list of N numbers and Q queries. Each query is specified by two 
numbers i and j; the answer to each query is the sum of every number between the 
range [i, j] (inclusive).

Note: the query ranges are specified using 0-based indexing.

Input
The first line contains N, the number of integers in our list (N <= 100,000). 
The next line holds N numbers that are guaranteed to fit inside an integer. 
Following the list is a number Q (Q <= 10,000). The next Q lines each contain 
two numbers i and j which specify a query you must answer (0 <= i, j <= N-1).

Output
For each query, output the answer to that query on its own line in the order 
the queries were made.

Example
Input:
3
1 4 1
3
1 1
1 2
0 2
Output:
4
5
6
"""

from functools import cmp_to_key
import math
from typing import AnyStr


n = int(input())
arr = [int(x) for x in input().split()]
q = int(input())
queries = []
for _ in range(q):
    l, r = input().split()
    queries.append((_, int(l), int(r)))

# Sorting the queries

root = math.ceil(math.sqrt(n))

def compare(gg1, gg2):
    if gg1[1]/root == gg2[1]/root:
        return gg1[2] - gg2[2]
    return gg1[1]/root - gg2[1]/root

queries.sort(key=cmp_to_key(compare))

answers = [0] * q

curr_l = 0
curr_r = -1
curr_ans = 0
for q in queries:
    index , l , r = q
    while curr_r < r:
        curr_r += 1
        curr_ans += arr[curr_r]
    
    while curr_l > l:
        curr_l -= 1
        curr_ans += arr[curr_l]
    while curr_l < l:
        curr_ans -= arr[curr_l]
        curr_l += 1
    while curr_r > r:
        curr_ans -= arr[curr_r]
        curr_r -= 1
    
    answers[index] = curr_ans

for gg in answers:
    print(gg)