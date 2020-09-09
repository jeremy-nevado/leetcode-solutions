class Solution:
    def max_branch(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        return 1 + max(self.max_branch(root.left), self.max_branch(root.right))

    def diameterOfBinaryTree(self, root):
        if not root: return 0
        if not root.left and not root.right: return 0
        return max(self.max_branch(root.left) + self.max_branch(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

