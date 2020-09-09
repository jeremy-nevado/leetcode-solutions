class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows - 1):
            curr = []
            for j in range(1, i+1):
                num = i // (i)
