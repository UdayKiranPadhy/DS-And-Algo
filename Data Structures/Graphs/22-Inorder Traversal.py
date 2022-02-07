class Solution(object):
    def inorderTraversal(self, root):
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)) if root else []
