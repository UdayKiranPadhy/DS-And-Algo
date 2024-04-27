"""

URL: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/

1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 
Example 1:

Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

Example 2:

Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

 
Constraints:

	2 <= n <= 100
	1 <= edges.length <= min(200, n * (n - 1) / 2)
	edges[i].length == 3
	0 <= ai < bi < n
	1 <= weighti <= 1000
	All pairs (ai, bi) are distinct.

"""
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N: int, edges: List[List[int]]) -> List[List[int]]:
        # edge = u , v ,w
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def mst(init=None, exclude=None):
            marked = [False] * N
            ans = 0
            pq = []  # min heap

            def visit(u):
                marked[u] = True
                for v, w in graph.get(u, []):
                    if exclude and u in exclude and v in exclude:
                        continue
                    else:
                        heappush(pq, [w, u, v])

            if init is not None:
                u, v, w = init
                ans += w
                visit(u) or visit(v)
            else:
                visit(0)
            while pq:
                w, u, v = heappop(pq)
                if marked[u] and marked[v]: continue
                ans += w
                if not marked[u]: visit(u)
                if not marked[v]: visit(v)
            return ans if all(marked) else float('inf')

        critical, pseudo = [], []
        ref = mst()
        for idx, edge in enumerate(edges):
            if mst(exclude=edge[:2]) > ref:
                critical.append(idx)
            elif mst(init=edge) == ref:
                pseudo.append(idx)
        return [critical, pseudo]