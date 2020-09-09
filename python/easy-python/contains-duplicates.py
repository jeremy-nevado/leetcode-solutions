class Solution:
    def containsDuplicate(self, nums):
        past = {}
        for num in nums:
            if num in past.keys():
                return True 
            past[num] = None
        return False
