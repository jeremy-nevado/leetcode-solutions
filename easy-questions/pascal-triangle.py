class Solution:
    def generate(self, numRows):
        res = [[1], [1, 1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [res[0]]
        if numRows == 2:
            return res
        for i in range(1, numRows - 1):
            curr = [1]
            for j in range(0, len(res[i]) - 1):
                curr.append(res[i][j] + res[i][j+1])  
            curr.append(1)
            res.append(curr)
        return res
