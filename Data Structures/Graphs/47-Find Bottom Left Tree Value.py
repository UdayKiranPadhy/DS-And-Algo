"""

513. Find Bottom Left Tree Value
Medium

https://leetcode.com/problems/find-bottom-left-tree-value/


Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []

        queue = deque([root])

        while queue:

            length = len(queue)
            level = []
            while length:
                popedNode = queue.popleft()
                if popedNode.left:
                    queue.append(popedNode.left)
                if popedNode.right:
                    queue.append(popedNode.right)
                level.append(popedNode.val)
                length -= 1
            res.append(level[::])
        return res[-1][0]
