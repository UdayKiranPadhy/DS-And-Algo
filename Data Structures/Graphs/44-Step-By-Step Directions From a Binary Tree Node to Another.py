"""

2096. Step-By-Step Directions From a Binary Tree Node to Another
Medium

https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue


"""


# Idea :
# This is a very nice problem as one require multiple concepts. Like

# Lowest Common Ancestor
# DFS : Tree Traversal and Backtracking (to get Path b/w nodes)
# First let us make couple of observations and note it down :

# How to get shortest distance/path b/w two node in Binary Tree?

# We need to find closest point(from nodes), where path from root to nodes intersect

# This is nothing but the LCA(Lowest Common Ancestor) of two nodes.

# Now, if we move from start node to LCA node, which direction we will follow : U(up) , L(left) or R(right) ?

# Here we can surely say since LCA always lie above the node, so we will move in upward direction.

# And there can also be a case when start node itself is LCA, so no need to worry in this case.

# Now coming back to our problem, we need to get shortest path from start -> destination , or

# in other words path from

#   "start -> LCA" + "LCA -> destination"

#   -> But we cannot find "start -> LCA" directly. i.e from bottom to up
#   -> What we can do instead is first find top to down path
#   		i.e "LCA -> start" , using normal tree traversal algo
#   -> and then convert it such that we move in upward direction. (Observation: 2)
# Thus, putting all these together. Lets write a step-by-step algorithm to get directions :

# First of all find the LCA node of start and destination.

# Then we need to get path from lca_to_start and from lca_to_destination.

# To get path from root -> node as a string, we will use traverse() function.

# In this we simply do a simple DFS ( kind of pre-order traversal)
# First explore left path, if node is found. Then return true.
# Otherwise backtrack and explore right path.
# Now that we have both paths, we will convert all chars in lca_to_start to U, since we will move upward.

# At last, concatenate both strings and return combined path.

# Lets see this through an example :

#   Given : start = 3, destination = 6

#   					  5   ---> LCA(3,6)
#   					/   \
#   				   1     2
#   				  /     /  \
#   	start <---	'3'   '6'    4
#   					   ^
#   					   |
#   				   destination

#   -> So here node '5' is LCA of start(3) and dest(3)
#   -> path from lca_to_start = '5 -> 1 -> 3' = "L L"
#   -> path from lca_to_dest = '5 -> 2 -> 6' = "R L"

#   Also, since we know that shortest path from
#   	# start-> destination = 'start -> LCA' + 'LCA -> destination'

#   So, we need to convert (reverse) `lca_to_start` = "U U" , as we move in upward direction

#   Therefore, final path = "U U" + "R L" = "U U R L"

# Complexity :

# Time : O(N + N + N) , N is number of nodes in binary tree

# Since first get LCA, so O(N) for that
# Then to get path from LCA to start and destination, so O(N)
# At last we convert lca_to_start string to 'U' and concatenate, so ~O(N)
# Space : O(N)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def lca(node):
            if node == None:
                return None
            if node and (startValue == node.val or destValue == node.val):
                return node
            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        def dfs(node, required, path):
            if not node:
                return False
            if node.val == required:
                return True
            path.append("L")
            if(dfs(node.left, required, path)):
                return True
            path.pop()

            path.append("R")
            if(dfs(node.right, required, path)):
                return True
            path.pop()

            return False
        common = lca(root)
        path1 = []
        dfs(common, startValue, path1)
        path2 = []
        dfs(common, destValue, path2)
        for i in range(len(path1)):
            path1[i] = "U"
        return "".join(path1) + "".join(path2)
