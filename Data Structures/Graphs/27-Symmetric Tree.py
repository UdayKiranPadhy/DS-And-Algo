"""

Symmetric Tree
Easy

7450

189

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

"""


# https://youtu.be/tNkDZvGsdAs

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def isMirror(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False

            return root1.val == root2.val and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
        return isMirror(root, root)
