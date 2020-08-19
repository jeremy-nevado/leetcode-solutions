class Solution:
    def rob(self, nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
            print(curr, prev)
        return curr

sol = Solution()
print(sol.rob([2, 4, 7, 1, 2, 3, 7, 9]))
