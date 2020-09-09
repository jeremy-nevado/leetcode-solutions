class Solution:
    def minPathSum(self, grid):
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            res = 0
            for i in range(len(grid)):
                res += grid[i][0]
            return res
        else:
            return min(self.minPathSum(grid[1]), self.minPathSum(grid[:][1]))

