import unittest
class Solution:
    def productExceptSelf(self, nums):
        res = []
        mul = 1
        for num in nums:
            res.append(mul)
            mul *= num
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= mul
            mul *= nums[i]
        return res

class TestSolution(unittest.TestCase):
    def test_product(self):
        self.assertEqual(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

if __name__ == '__main__':
    unittest.main()
