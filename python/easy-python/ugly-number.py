import unittest

class Solution:
    def isUgly(self, num):
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1

class Testsolution(unittest.TestCase):
    def testisugly(self):
        self.assertTrue(Solution().isUgly(8))
        self.assertTrue(Solution().isUgly(30))
        self.assertFalse(Solution().isUgly(14))

if __name__ == '__main__':
    unittest.main()
