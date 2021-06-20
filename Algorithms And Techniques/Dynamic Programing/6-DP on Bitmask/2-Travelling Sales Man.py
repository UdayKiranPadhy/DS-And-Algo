"""

Given a list of cities and distances between each pair of cities, what is
the shortest possible route that visits wach cities each city and returns
to the origin city.

Example 1
[[0,10,15,20],
 [5,0,9,10],
 [6,13,0,12],
 [8,8,9,0]]

"""

from functools import lru_cache
import sys


@lru_cache(None)
def travellingSalesMan(i, mask, n):
    # Base Case
    if i == n and mask == 0:
        return cost[i-1][1]

    min_distance = sys.maxsize
    for j in range(n):
        if(mask & (1 << j)):
            min_distance = min(
                min_distance, cost[i][j] + travellingSalesMan(i+1, (mask ^ (1 << j)), n))

    return min_distance


def main():
    n = int(input())  # No. Of Cities
    for i in range(n):
        cost.append([int(x)
                    for x in input().strip().split(" ")])  # City Distances
    return travellingSalesMan(0, (1 << n)-1, n)


if __name__ == '__main__':
    for t in range(int(input())):
        cost = []
        print(main())
