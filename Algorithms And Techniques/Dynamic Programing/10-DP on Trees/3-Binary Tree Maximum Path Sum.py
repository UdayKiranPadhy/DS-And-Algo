"""
link :- https://leetcode.com/problems/binary-tree-maximum-path-sum/
Date : 20/6/2021 ,mrng 6:45

124. Binary Tree Maximum Path Sum
Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

All cases 
[1,2,3]
[-10,9,20,null,null,15,7]
[-3]
[1,-2,3]
[-1,-2,10,-6,null,-3,-6]
[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]

"""


# My trails
# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def thSum(self, root: TreeNode) -> int:
        result = -sys.maxsize

        def dfs(root):
            nonlocal result
            if root == None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            op1 = max(max(l, r, 0) + root.val, root.val)
            op2 = max(op1, l + r + root.val, l, r)
            return op2

        return dfs(root)


# Original Answer
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = root.val

        def maxi(root):
            if root == None:
                return 0
            lr = maxi(root.left)
            ri = maxi(root.right)
            self.maximum = max(self.maximum, root.val + lr +
                               ri, root.val + lr, root.val + ri, root.val)
            return max(root.val + max(lr, ri), root.val)
        maxi(root)
        return self.maximum
