"""
743. Network Delay Time
Medium

You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the 
source node, vi is the target node, and wi is the time it takes for a signal to 
travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n 
nodes to receive the signal. If it is impossible for all the n nodes to receive 
the signal, return -1. 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

"""
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        visited = set()
        graph = {}
        for i in range(1, n + 1):
            graph[i] = []
        for i in times:
            u, v, w = i
            if u in graph:
                graph[u].append([v, w])

        minH = [[0, k]]
        distance = [float('inf')] * (n)
        distance[k - 1] = 0
        while minH:
            popedElement = heapq.heappop(minH)
            weight, index = popedElement
            visited.add(index)
            for neibour in graph[index]:
                Vertex, edgeWeight = neibour
                if Vertex in visited:
                    continue
                newDist = distance[index - 1] + edgeWeight
                if newDist < distance[Vertex - 1]:
                    distance[Vertex - 1] = newDist
                    heapq.heappush(minH, [newDist, Vertex])

        return -1 if max(distance) == float('inf') else max(distance)