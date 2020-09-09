class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        right, left = None, None
        if p == root:
            return p
        if q == root:
            return q
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if right and left:
            return root
        elif left or right:
            return left or right
        else:
            return None
