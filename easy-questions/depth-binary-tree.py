class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0 
        else:
            return max(1 + self.maxDepth(root.right), 1 + self.maxDepth(root.left))
