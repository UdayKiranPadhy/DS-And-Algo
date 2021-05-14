"""
Sometimes a graph is split into multiple components.
It's useful to be able to identify and count these components.
"""

"""
We can use a dfs to identify components 1st , make sure all the nodes are labeled from [0,n)
where n is the no. of nodes.

Algo:
Start dfs at every node (except if it's already been visited) and make all reachable nodes as being part
of some component.
"""

n = 18  # No. of nodes in the graphs
g = {
    0: [13, 14, 8, 4],
    1: [5],
    2: [15, 9],
    3: [9],
    4: [8, 0],
    5: [1, 17, 16],
    6: [7, 11],
    7: [6, 11],
    8: [4, 0, 14],
    9: [3, 15, 2],
    10: [15],
    11: [6, 7],
    12: [],
    13: [14, 0],
    14: [8, 0, 13],
    15: [10, 2, 9],
    16: [5],
    17: [5],
}
# Adjacency list representation of the graph

count = 0
components = [0] * n
visited = [False] * n


def find_components():
    global count
    global components
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return (count, components)


def dfs(at):
    visited[at] = True
    components[at] = count
    for next in g[at]:
        if not visited[next]:
            dfs(next)


print(find_components())
