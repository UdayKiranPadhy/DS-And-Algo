"""

847. Shortest Path Visiting All Nodes
Hard

1421

104

Add to List

Share
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.


"""

# Solution From where i learnt 
# https://www.youtube.com/watch?v=Ut-keVP8H8E&ab_channel=ProgrammingLivewithLarry


from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        INF = 10 ** 9 
        N = len(graph)
        dist = [[INF] * N for _ in range(N)]

        for i,edges in enumerate(graph):
            dist[i][i] = 0
            for edge in edges:
                dist[i][edge] = 1
        
        # Floyd Warshell Algo
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        @cache
        def visit(node,visited):
            if visited == (1<<N) - 1:
                return 0
            
            best = INF

            for i in range(N):
                if (1<<i) & visited == 0:
                    best = min(best,visit(i,visited | (1<<i))+ dist[node][i])
            return best
        
        best = INF

        for i in range(N):
            best = min(best , visit(i,(1<<i)))
        return best