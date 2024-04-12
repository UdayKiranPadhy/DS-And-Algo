"""
https://leetcode.com/problems/subtree-of-another-tree/


572. Subtree of Another Tree
Easy

8075

494

Add to List

Share
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

"""
from typing import Optional


# Definition for a binary tree node.
# Time complexity is O(mn), where m and n are number of nodes in each tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isEqual(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val == node2.val:
                return isEqual(node1.left,node2.left) and isEqual(node1.right,node2.right)

        def traverse(node, subTree):
            if isEqual(node,subTree):
                return True
            return traverse(node.left, subTree) or traverse(node.right,subTree)

        return traverse(root,subRoot)

# KMP Algo
class Solution:
    def isSubtree(self, s, t):
        def dfs(root):
            if not root: return "#"
            return str(root.val) + ":" + dfs(root.left) + ":" + dfs(root.right)
        return ":" + dfs(t) in ":" + dfs(s)

