class Solution:
  def removeDuplicates(self, nums):
    temp = []
    for num in nums:
      if num not in temp: temp.append(num)
    nums = temp
    return len(nums), nums

sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))