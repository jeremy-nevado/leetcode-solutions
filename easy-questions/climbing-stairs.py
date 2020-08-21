import unittest

class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
        
    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

class TestSolution(unittest.TestCase):
    def test_climbstairs(self):
        self.assertEqual(Solution().climbStairs(4), 5)
        self.assertEqual(Solution().climbStairs(3), 3)
        self.assertEqual(Solution().climbStairs(2), 2)
        self.assertEqual(Solution().climbStairs(38), 112)

if __name__ == '__main__':
    unittest.main()
