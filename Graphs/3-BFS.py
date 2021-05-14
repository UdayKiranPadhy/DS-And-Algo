"""
finding the shortest path on unweighted graphs
Explores the neighbour's nodes first, before moving to the next level neighbours
"""

n = 13  # number of nodes
g = {
    0: [9, 7, 11],
    1: [10, 8],
    2: [12, 3],
    3: [2, 7, 4],
    4: [3],
    5: [6],
    6: [7, 5],
    7: [3, 6, 11, 0],
    8: [1, 9, 12],
    9: [10, 8, 0],
    10: [1, 9],
    11: [0, 7],
    12: [8, 2],
}


def bfs(s, e):
    prev = solve(s)
    # [None, 10, 3, 7, 3, 6, 7, 0, 9, 0, 9, 0, 8] prev

    # reconstruct returns a list of shortest path using nodes
    return reconstruct(s, e, prev)


def reconstruct(s, e, prev):
    path = []
    path.append(e)
    while e != s:
        e = prev[e]
        path.append(e)
    path.reverse()
    return path


def solve(s):
    q = []
    q.append(s)
    visited = [False] * n
    visited[s] = True
    prev = [None] * n
    while len(q) != 0:
        node = q.pop(0)
        neighbours = g[node]
        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                prev[next] = node
    return prev


print(bfs(0, 12))
