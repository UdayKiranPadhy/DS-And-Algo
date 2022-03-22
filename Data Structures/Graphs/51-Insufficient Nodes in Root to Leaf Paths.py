"""

1080. Insufficient Nodes in Root to Leaf Paths
Medium

https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
-105 <= Node.val <= 10^5
-109 <= limit <= 10^9


Testcases to solve
[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]
1
[5,4,8,11,null,17,4,7,1,null,null,5,3]
22
[1,2,-3,-5,null,4,null]
-1
[10,5,10]
21

"""



# Definition for a binary tree node.
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(node,total):
            if not node:
                return False
            if node and not node.left and not node.right:
                if total + node.val < limit:
                    return False
                return True
            left = dfs(node.left,total + node.val)
            right = dfs(node.right,total + node.val)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right
        
        found = dfs(root,0)
        return root if found else None