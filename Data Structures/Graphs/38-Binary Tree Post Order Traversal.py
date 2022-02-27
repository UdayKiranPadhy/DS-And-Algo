"""

145. Binary Tree Postorder Traversal
Easy

3812

135

Add to List

Share
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
# https://leetcode.com/problems/binary-tree-postorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None:
            return ans

        def go(root):
            if root == None:
                return
            go(root.left)
            go(root.right)
            ans.append(root.val)
        go(root)
        return ans

# Iterative Solution
# https://www.youtube.com/watch?v=NzIGLLwZBS8&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=13&ab_channel=takeUforward


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None:
            return ans
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                temp = stack[-1].right
                if temp == None:
                    temp = stack.pop()
                    ans.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        ans.append(temp.val)
                else:
                    node = temp
        return ans
