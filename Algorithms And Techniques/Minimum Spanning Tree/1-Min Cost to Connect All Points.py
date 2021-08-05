"""

1584. Min Cost to Connect All Points
Medium

You are given an array points representing integer coordinates of some 
points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are 
connected if there is exactly one simple path between any two points.
 
Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.


Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Example 3:
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4


Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000

Example 5:

Input: points = [[0,0]]
Output: 0
 
Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

"""
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)

        adj = {i: [] for i in range(N)}

        # Filling the graph
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prims Algo
        res = 0
        visited = set()
        minH = [[0, 0]]

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res = res + cost
            visited.add(i)
            for cost, next_index in adj[i]:
                if next_index not in visited:
                    heapq.heappush(minH, [cost, next_index])
        return res
