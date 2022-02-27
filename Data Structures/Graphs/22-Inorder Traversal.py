class Solution(object):
    def Traversal(self, root):
        return (self.Traversal(root.left) + [root.val] + self.Traversal(root.right)) if root else []
