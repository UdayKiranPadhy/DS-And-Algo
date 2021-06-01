"""

Problem Statement

Let there be N workers and N jobs. Any worker can be assigned to perform any 
job, incurring some cost that may vary depending on the work-job assignment. 
It is required to perform all jobs by assigning exactly one worker to each 
job and exactly one job to each agent in such a way that the total cost of 
the assignment is minimized.

Input Format
Number of workers and job: N
Cost matrix C with dimension N*N where C(i,j) is the cost incurred on 
assigning ith Person to jth Job.

Sample Input
4

[
9 2 7 8
6 4 3 7
5 8 1 8
7 6 9 4
]

Sample Output
13

Constraints
N <= 20

"""


"""
Solution Explanation :- https://www.youtube.com/watch?v=685x-rzOIlY&list=PLb3g_Z8nEv1icFNrtZqByO1CrWVHLlO5g&index=5&ab_channel=KartikArora

"""




from functools import lru_cache
import sys
@lru_cache(None)
def mincost(i, mask, n):
    if i == n:
        return 0
    mini = sys.maxsize
    for j in range(n):
        if(mask & (1 << j)):
            mini = min(mini, cost[j][i] + mincost(i+1, mask ^ (1 << j), n))
    return mini


def main():
    n = int(input())
    for i in range(n):
        cost.append([int(x) for x in input().split(" ")])
    return mincost(0, (1 << n)-1, n)


if __name__ == '__main__':
    for i in range(int(input())):
        cost = []
        print(main())
