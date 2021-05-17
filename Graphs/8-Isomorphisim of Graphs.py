"""
Two Graphs are said to be isomorphic if they have same structure nodes need not to be unique.
"""


def treesAreIsomorphic(tree1, tree2):
    tree1_center = treecenters(tree1)
    tree2_center = treecenters(tree2)

    tree1_root = rootTree(tree1, tree1_center)
    tree1_encoded = encoder(tree1_root)
    for center in tree2_center:
        tree2_root = rootTree()
