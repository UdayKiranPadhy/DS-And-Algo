"""
Height of Binary Tree 

Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2

Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   

Your Task:
You don't need to read input or print anything. Your task is to complete the function 
height() which takes root node of the tree as input parameter and returns an integer 
denoting the height of the tree. If the tree is empty, return 0. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^5

Company Tags
 Amazon Cadence India CouponDunia D-E-Shaw FactSet 
 FreeCharge MakeMyTrip Monotype Solutions Snapdeal 
 Synopsys Teradata VMWare Zoho Microsoft
Topic Tags
 Tree

"""


# Algorithm:

# If node is null then return 0.
# Else we call the recursive function, height for left and right subtree and choose their maximum.
# We also add 1 to the result which indicates height of root of the tree.

tree = {6: [2, 7], 1: [], 3: [], 5: [], 8: [], 2: [1, 4], 4: [3, 5], 7: [9], 9: [8]}


class Solution:

    # Function to find the height of a binary tree.
    def height(self, node):

        # if node is null, we return 0.
        if node is None:
            return 0

        # else we call the recursive function, height for left and right
        # subtree and choose their maximum. we also add 1 to the result
        # which indicates height of root of the tree.
        return 1 + max(self.height(node.left), self.height(node.right))
