class Solution:
    def generateMatrix(self, n):
        lst = range(n*n)
        matrix = []
        curr_row = -1
        for num in lst:
            if num%n == 1:
                matrix.append([])
                curr_row += 1



