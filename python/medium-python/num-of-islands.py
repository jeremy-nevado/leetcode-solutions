class Solution:
    def visit(self, grid, i, j):
        grid[i][j] = 2
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.visit(grid, i-1, j)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.visit(grid, i, j-1)
        if i+1 < len(grid) and grid[i+1][j] == "1":
            self.visit(grid, i+1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] == "1":
            self.visit(grid, i, j+1)
        return

    def numIslands(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.visit(grid, i, j)
                    print(grid)
        return res


sol = Solution()


print(sol.numIslands([["1","0","1"],["0","1","0"],["1","0","1"]]))
