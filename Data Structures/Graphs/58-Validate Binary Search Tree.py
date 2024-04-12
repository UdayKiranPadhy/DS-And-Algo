"""
https://leetcode.com/problems/validate-binary-search-tree/

98. Validate Binary Search Tree
Medium

16533

1355

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minimum, maximum):
            if minimum >= node.val or node.val >= maximum:
                return False
            left = right = True
            if node.left:
                left = validate(node.left,minimum,node.val)
            if node.right:
                right = validate(node.right,node.val,maximum)
            return left & right

        return validate(root, -float('inf'), float('inf'))


root = TreeNode(2,TreeNode(1),TreeNode(2))

model = Solution()
print(model.isValidBST(root))