class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        accum = [root.val]

    def helper(self, left, right, accum, direction):
        if left is None:
            t
