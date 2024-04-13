"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

14673

490

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre_begin, pre_end, in_begin, in_end):
            if pre_end - pre_begin <= 0: return None
            root = TreeNode(preorder[pre_begin])
            index = mappings[preorder[pre_begin]]
            root.left = dfs(pre_begin + 1, pre_begin + 1 + index - in_begin, in_begin, index)
            root.right = dfs(pre_begin + index - in_begin + 1, pre_end, index + 1, in_end)
            return root

        mappings = {element: idx for idx, element in enumerate(inorder)}
        return dfs(0, len(preorder), 0, len(inorder))
