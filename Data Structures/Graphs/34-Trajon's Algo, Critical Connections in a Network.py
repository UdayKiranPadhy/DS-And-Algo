"""
https://leetcode.com/problems/critical-connections-in-a-network/description/

1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server 
connections forming a network where connections[i] = [ai, bi] represents a connection 
between servers ai and bi. Any server can reach other servers directly or indirectly 
through the network.

A critical connection is a connection that, if removed, will make some servers unable 
to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.

"""

# Solution
# In my opinion it is very difficult problem if you are not familiar with graph theory. 
# What is actually asked here is to find all so-called bridges in given graph, 
# here you can see detailed explanation of the very classical 
# algorithm: https://cp-algorithms.com/graph/bridge-searching.html

# Here I give some details about the code, using the link I provided. The key observation about the bridge is:


from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, N: int, connections: List[List[int]]) -> List[List[int]]:
        timer = 0
        t_entry = [-1] * N
        low_link = [-1] * N
        visited = [False] * N
        result = []

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int = -1):
            nonlocal timer
            visited[node] = True
            t_entry[node] = low_link[node] = timer
            timer += 1

            for neibour in graph[node]:
                if neibour == parent:
                    continue
                if visited[neibour]:
                    low_link[node] = min(low_link[node], t_entry[neibour])
                else:
                    dfs(neibour, node)
                    low_link[node] = min(low_link[node], low_link[neibour])
                    if low_link[neibour] > t_entry[node]:
                        result.append([node, neibour])

        for i in range(N):
            if not visited[i]:
                dfs(i)

        return result
