class Solution:
    def maxArea(self, height):
        L, R, width, area = 0, len(height) - 1, len(height) - 1, 0
        for i in range(width, 0, -1):
            area = max(area, i * min(height[L], height[R]))
            if height[L] < height[R]:
                L = L + 1
            else:
                R = R - 1
        return area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

