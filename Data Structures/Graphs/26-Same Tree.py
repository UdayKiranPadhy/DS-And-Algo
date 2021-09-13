"""

100. Same Tree
Easy

4003

102

Add to List

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""

# https://leetcode.com/problems/same-tree

# As it given in problem statement: two binary trees are considered the same if
# they are structurally identical and the nodes have the same value. So all we
# need to do is to check this condition recursively:

# If we reached node p in one tree and q in another tree (we allow to reach None nodes),
# we need to consider 3 cases:

# If one of them do not exist and another exist, we return False.
# If two of them are equal to None, we return True.
# If none of two above condition holds, we look at children and return True only if values of nodes are equal and if True holds for left and right subtrees.
# Complexity: time complexity is O(n), because we traverse all tree. Space complexity is O(h) to keep recursion stack. Time complexity can be imporved a bit, if we use helper function and directly return False if we found difference between trees.


class Solution:
    def isSameTree(self, p, q):
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
