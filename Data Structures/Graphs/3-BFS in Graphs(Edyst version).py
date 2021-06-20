"""
BFS in Graphs
Given N nodes and E edges of a graph where ith element of the array U is connected 
to ith element of V.

Return the nodes while doing BFS starting from node 1.

Note: Use recursive approach.
Example :
Input :
N = 5, E = 4
U = [1, 1, 1, 3]
V = [2, 3, 4, 5]

Output :
[1, 2, 3, 4, 5]


                 1
              /  |  \
            2    3    4 
                 | 
                 5

"""


class Solution:
    def BFS(self, N, E, U, V):
        # Converting Given two lists in form of adjaency lists
        g = {}
        for i in range(1, N + 1):
            g[i] = []
            for j in range(len(U)):
                if i == U[j]:
                    g[i].append(V[j])
        queue = []
        queue.append(U[0])
        while len(queue) != 0:
            node = queue.pop(0)
            print(node)
            for i in g[node]:
                queue.append(i)

model = Solution()
model.BFS(5, 4, [1, 1, 1, 3], [2, 3, 4, 5])
