"""

94. Binary Tree Inorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?


"""

# Recursive Solution

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root == None:
            return ans

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans

# Iterative Solution


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root == None:
            return ans
        node = root
        stack = []
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    break
                popedElement = stack.pop()
                ans.append(popedElement.val)
                node = popedElement.right
        return ans
