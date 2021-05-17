"""
https://codeforces.com/blog/entry/17974

https://www.geeksforgeeks.org/graph-measurements-length-distance-diameter-eccentricity-radius-center/

https://towardsdatascience.com/graph-theory-center-of-a-tree-a64b63f9415d

Find the suitable node which can be taken as a root node (or find the center of the graph).

"""

g = {
    0: [1],
    1: [0, 2],
    2: [1, 9, 3, 6],
    3: [2, 4, 5],
    4: [3],
    5: [3],
    6: [2, 8, 7],
    7: [6],
    8: [6],
    9: [2],
}


def treecenters(g):
    n = len(g)
    degree = [0] * n
    leaves = []
    for i in range(n):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
            degree[i] = 0
    count = len(leaves)
    while count < n:
        new_leaf = []
        for node in leaves:
            for neibours in g[i]:
                degree[neibours] -= 1
                if degree[neibours] == 1:
                    new_leaf.append(neibours)
                degree[node] = 0
            count += len(new_leaf)
            leaves = new_leaf
    return leaves


print(treecenters(g))
