import unittest

class Solution:
  def removeDuplicates(self, nums):
    temp = []
    for num in nums:
      if num not in temp: temp.append(num)
    nums = temp
    return len(nums), nums

class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        self.assertEqual(Solution().removeDuplicates([1, 2, 3, 1, 5, 3, 1, 8, 10, 100, 92, 83, 83, 71, 1, 1, 1, 1]), (10, [1, 2, 3, 5, 8, 10, 100, 92, 83, 71]))
        self.assertEqual(Solution().removeDuplicates([1, 1, 2, 2, 3, 3]), (3, [1, 2, 3]))

if __name__ == '__main__':
    unittest.main()

