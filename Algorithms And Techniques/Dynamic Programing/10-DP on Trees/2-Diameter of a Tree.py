"""
Link :- https://leetcode.com/problems/-of-binary-tree/
Date :- 19/06/2021

543.  of Binary Tree

Given the root of a binary tree, return the length of the  of the tree.

The  of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges 
between them.


Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100

"""


"""
Solution approach

There are three cases 
case 1 :- The  may completely lie on the left sub tree
case 2 :- The  may completely lie on the right sub tree
case 3 :- The  may pass through the root of the tree.
so we have to see for all the probable cases here.
Approach: we are going to use recursion
h1 = calculate the height of the left sub tree.
h2 = calculate the height of the right sub tree.
op1 = h1+h2(as discussed the  may paas through the root.)
op2 = (root->left)// recursively.
op3 = (root->right) //recursively.
return max of op1,op2,op3;

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def OfBinaryTree(self, root: TreeNode) -> int:

        def height(root: TreeNode):
            if root == None:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)

        def FindBinary(root: TreeNode):
            if root == None:
                return 0
            h1 = height(root.left)
            h2 = height(root.right)
            op1 = h1+h2
            op2 = FindBinary(root.left)
            op3 = FindBinary(root.right)
            return max(op1, op2, op3)

        return FindBinary(root)


# Optimal Approach
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = -1

        def height(root):

            if root == None:
                return 0
            lr = height(root.left)
            ri = height(root.right)
            self.maximum = max(self.maximum, lr + ri)

            return 1 + max(lr, ri)
        height(root)
        return self.maximum
