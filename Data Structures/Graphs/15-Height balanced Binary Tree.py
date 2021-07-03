"""

110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ 
in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if root == None:
                return 0
            else:
                return max(height(root.left), height(root.right))+1

        def gg(root):
            if root == None:
                return True

            if gg(root.left) == False:
                return False
            if gg(root.right) == False:
                return True

            lh = height(root.left)
            rh = height(root.right)
            if abs(lh-rh) <= 1:
                return True
            else:
                False

        return gg(root)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.answer = True

        def dfs(root):
            l, r = 0, 0

            if root.left:
                l += dfs(root.left)
            if root.right:
                r += dfs(root.right)
            if abs(r-l) > 1:
                self.answer = False

            # print(root.val, r, l)
            return max(r, l) + 1
        dfs(root)
        return self.answer
