"""
Explore nodes and edges
Time Complexity O(V+E)
Count connected Components , determine connectivity , or find bridges / articulation points.
As the name suggests , a dfs goes depth 1st into a graph without regard for which edge it takes
until it cant go any further at which point it backtracks and continues .

"""

n = 12  # number of node
g = {
    0: [1, 9],
    1: [0, 8],
    2: [3],
    3: [2, 4, 5, 7],
    4: [3],
    5: [3, 6],
    6: [7, 5],
    7: [8, 3, 6, 10, 11],
    8: [1, 9, 7],
    9: [0, 8],
    10: [7, 11],
    11: [7, 10],
}
# Adjacency List representation of graph

visited = [False] * n

def DFS(at):
    if visited[at]:
        return
    visited[at] = True
    print(at)
    neighbors = g[at]
    for next in neighbors:
        DFS(next)


start_node = 0
DFS(start_node)

"""
Actual Representation can differ from user to user, In internet you can find various other representations
I am happy with this one.
"""
