"""
Problem Statement :https://www.spoj.com/problems/RMQSQ/

You are given a list of N numbers and Q queries. Each query is specified by two 
numbers i and j; the answer to each query is the minimum number between the 
range [i, j] (inclusive).

Note: the query ranges are specified using 0-based indexing.

Input
The first line contains N, the number of integers in our list (N <= 100,000). The next line 
holds N numbers that are guaranteed to fit inside an integer. Following the list is a 
number Q (Q <= 10,000). The next Q lines each contain two numbers i and j which 
specify a query you must answer (0 <= i, j <= N-1).

Output
For each query, output the answer to that query on its own line in the order the 
queries were made.

Example
Input:
3
1 4 1
2
1 1
1 2
Output:
4
1


"""
import math

n = int(input())

arr = [int(x) for x in input().split()]

queries = []

for _ in range(int(input())):
    l, r = input().split()
    queries.append((int(l), int(r)))

root = math.ceil(math.sqrt(n))

blocks = [pow(10, 9)] * root

for i in range(n):
    blocks[i//root] = min(blocks[i//root], arr[i])

for q in queries:
    l, r = q
    ans = pow(10, 9)
    while l <= r:
        if l % root == 0 and l+root-1 <= r:
            ans = min(ans, blocks[l//root])
            l += root
        else:
            ans = min(ans, arr[l])
            l += 1
    print(ans)
