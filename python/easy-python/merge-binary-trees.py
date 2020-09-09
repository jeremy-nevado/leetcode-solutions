import unittest

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.left = left
        self.right= right

class Solution:
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t1.val = t2.val + t1.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2

class TestSolution(unittest.TestCase):
    def test_mergetrees(self):
        t1 = TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(2))
        t2 = TreeNode(1, TreeNode(2), TreeNode(2))
        self.assertEqual(Solution().mergeTrees(t1, t2), TreeNode(3, TreeNode(5, TreeNode(4)), TreeNode(2)))

if __name__ == '__main__':
    unittest.main()
