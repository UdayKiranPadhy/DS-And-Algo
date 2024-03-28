"""

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has both p and 
q as descendants (where we allow a node to be a descendant of itself).” 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.

"""

# Algorith -1
# 1) Store path of root to n1 in an array
# 2) Store path of root to n2 in an array
# 3) LCA is the common element in the arrays just before the mismatch.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findnode(root, p, array1):
        if root == None:
            return False
        if root.val == p.val:
            array1.append(root)
            return True
        if Solution.findnode(root.left, p, array1):
            array1.append(root)
            return True
        if Solution.findnode(root.right, p, array1):
            array1.append(root)
            return True

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        array1 = []
        Solution.findnode(root, p, array1)
        array1.reverse()
        array2 = []
        Solution.findnode(root, q, array2)
        array2.reverse()
        for i in range(1, len(array1) if len(array1) < len(array2) else len(array2)):
            if array1[i].val == array2[i].val:
                continue
            else:
                return array1[i - 1]
        return array1[-1] if len(array1) < len(array2) else array2[-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack_p = []
        stack_q = []

        def findpath(root, search, stack):
            if root == None:
                return False
            stack.append(root)

            if root.val == search.val:
                return True

            if findpath(root.left, search, stack) or findpath(root.right, search, stack):
                return True

            stack.pop()
            return False

        findpath(root, p, stack_p)
        findpath(root, q, stack_q)
        index = 0
        for i in range(1, len(stack_p) if len(stack_p) < len(stack_q) else len(stack_q)):
            if stack_p[i].val != stack_q[i].val:
                return stack_p[i - 1]
            index = i
        return stack_p[index]


# Method-2 Recursive
# # Approach:
# We will use recursion to expand and extract out all the subtree possibilities,

# Cases To Consider:
# 1) If the current subtree contains both the nodes then return the root node of current subtree as answer.
# 2) If the current subtree does not contain both the nodes then return NULL, as this cannot be the LCA,
# 3) If the current subtree contain only one node , then result will be itself that node.

# # Note:
# It is mentioned that both the nodes exist in the tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def anis(root):
            if root == None:
                return None
            if root.val == p or root.val == q:
                return root
            left = anis(root.left)
            right = anis(root.right)
            if left != None and right != None:
                return root
            elif left != None:
                return left
            return right
        return anis(root)

