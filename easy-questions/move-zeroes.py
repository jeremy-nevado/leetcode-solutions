class Solution:
    def moveZeroes(self, nums):
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(nums.pop(i))
        return nums + zeroes
