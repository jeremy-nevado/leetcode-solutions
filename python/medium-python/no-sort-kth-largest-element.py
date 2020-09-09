import unittest

class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        for i in range(k - 1):
            nums.remove(max(nums))
        return max(nums)

class TestSolution(unittest.TestCase):
    def test_findkthlargest(self):
        self.assertEqual(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
        self.assertEqual(Solution().findKthLargest([3,2,1,5,6,4], 2), 5)

if __name__ == '__main__':
    unittest.main()
