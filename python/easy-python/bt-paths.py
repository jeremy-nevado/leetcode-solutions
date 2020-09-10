import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self. left = left
        self. right = right 


class Solution:
    def binaryTreePaths(self, root):
        right, left= [], []
        if not root:
            return []

        if not root.left and not root.right:
            return ["%r"%root.val]

        if root.right:
            right_sols = self.binaryTreePaths(root.right)
            for sol in right_sols:
                sol = "%r->"%root.val + sol
                right.append(sol)

        if root.left:
            left_sols = self.binaryTreePaths(root.left)
            for sol in left_sols:
                sol = "%r->"%root.val + sol
                left.append(sol)
        return right + left 

class TestSolution(unittest.TestCase):
    def testBTP(self):
        tree = TreeNode(2, TreeNode(1, None, None), TreeNode(1, None, None))
        self.assertEqual(Solution().binaryTreePaths(tree), ["2->1", "2->1"])

if __name__ == '__main__':
    unittest.main()
