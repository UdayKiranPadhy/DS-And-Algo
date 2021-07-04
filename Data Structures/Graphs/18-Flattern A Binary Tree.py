"""
Date :-4/7/21
Source :- https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

114. Flatten Binary Tree to Linked List
Medium

4775

421

Add to List

Share
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

"""


# Solution
# When ever our problem is releated to changing the links our goto choice is PostOrder Traversal.
# Because in post order 1st we travrse left , then right , and atlast we traverse the root
# So Once the left and right have been processed we change the root, so its helpful in changing the links
# But here as we saw the left Node shall be None so instead of Left Right root , we
# will traverse in Right Left Root
# For Each of the node 1st we will fix the right subtree and then the left subtree as None and
# then we can process the root

prev = None


def flat(root):
    if root == None:
        return
    flat(root.right)
    flat(root.left)
    root.right = prev
    root.left = None
    prev = root

# Time Complexity : O(N)
# Space Complexity : O(1)


# Using Stack
stack = []


def Flat2(root):
    if root == None:
        return
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if len(stack) != 0:
            node.right = stack[-1]
        node.left = None
