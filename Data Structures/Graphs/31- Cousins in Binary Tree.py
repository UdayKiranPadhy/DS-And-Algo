"""

993. Cousins in Binary Tree
Easy

Given the root of a binary tree with unique values and the values of two different nodes 
of the tree x and y, return true if the nodes corresponding to the values x and y in the 
tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k 
node are at the depth k + 1.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


"""


# Bredth First Search

# Definition for a binary tree node.
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = Deque()
        level = 0
        queue.append((None, root, level))
        level += 1
        x_found = False
        y_found = False
        while queue:
            for i in range(len(queue)):
                popedElement = queue.popleft()
                if popedElement[1].left:
                    queue.append(
                        (popedElement[1].val, popedElement[1].left, level))
                if popedElement[1].right:
                    queue.append(
                        (popedElement[1].val, popedElement[1].right, level))
                if popedElement[1].val == x:
                    x_found = True
                    x_parent = popedElement[0]
                if popedElement[1].val == y:
                    y_found = True
                    y_parent = popedElement[0]
            if x_found and y_found:
                if x_parent != y_parent:
                    return True
                else:
                    return False
            if x_found and not y_found:
                return False
            if y_found and not x_found:
                return False
