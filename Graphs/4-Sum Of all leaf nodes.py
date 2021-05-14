"""

Sum of Leaf Nodes 
Given a Binary Tree of size N. The task is to complete the function sumLeaf(), that 
should return the sum of all the leaf nodes of the given binary tree.

Input:
First line of input contains number of testcases T. For each testcase, there will 
be two lines, first of which containing the number of edges (between two nodes) 
in the tree. Next line contains N pairs (considering a and b) with a 'L' (means 
node b on left of a) or 'R' (means node b on right of a) after a and b.

Output:
For each testcase, there will be a single line containing the 
sum of all leaf nodes in the tree.

User Task:
The task is to complete the function sumLeaf() which takes root reference as argument 
and returns the sum of all leaf nodes.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
2
1 2 L 1 3 R
5
10 20 L 10 30 R 20 40 L 20 60 R 30 90 L

Output:
5
190

Explanation:
Testcase 1: Leaf nodes in the tree are 2 and 3, and their sum is 5.
 

Topic Tags
 Tree

"""

# Tree representation
tree = {6: [2, 7], 1: [], 3: [], 5: [], 8: [], 2: [1, 4], 4: [3, 5], 7: [9], 9: [8]}


def SumOfLeafNodes(node):
    if node == None:
        return 0
    if isleaf(node):
        return node
    total = 0
    for child in tree[node]:
        total += SumOfLeafNodes(child)
    return total


def isleaf(node):
    return True if len(tree[node]) == 0 else False


print(SumOfLeafNodes(6))



"""

Actualy Solution
"""

# Python3 Program to find the 
#sum of leaf nodes of a binary tree
  
  
 # Class for node creation
class Node:
      
     # Constructor
    def __init__(self, data):             
        self.data = data
        self.left = None
        self.right = None
  
# Utility function to calculate 
# the sum of all leaf nodes
def leafSum(root):
    global total
    if root is None:
        return
    if (root.left is None and root.right is None):
        total += root.data
    leafSum(root.left)
    leafSum(root.right)

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(8)
# Variable to store the sum of leaf nodes
    total = 0
    # leafSum(root)
# Printing the calculated sum
    # print(total)