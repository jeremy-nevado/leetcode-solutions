class Solution:
    def searchRange(self, nums, target):
        a, b = -1, -1 
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
        if a == -1:
            return [-1, -1]
        for i in range(len(nums), -1, -1):
            if nums[i] == target:
                b = i
                break
        return [a, b]
