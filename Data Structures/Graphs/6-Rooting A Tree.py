"""

Given a undirected graph and node which is to be the root node

"""


class TreeNode:
    def __init__(self, id, parent, children=[]):
        self.id = id
        self.parent = parent
        self.children = children


g = {0: [5, 1, 2], 5: [4, 6], 1: [], 4: [], 6: [], 2: [3], 3: []}


def rootNode(g, rootId=0):
    root = TreeNode(rootId, None, [])
    return BuildTree(g, root, None)


def BuildTree(g, node, parent):
    for childid in g[node.id]:
        if parent != None and childid == parent.id:
            continue
        child = TreeNode(childid, node, [])
        node.children.append(child)
        BuildTree(g, child, node)
    return node


print(rootNode(g, 0).children)
print()
print(rootNode(g, 0))
