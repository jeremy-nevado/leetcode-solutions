class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = matrix.pop(0)
        row_rev, col_rev, row = True, False, False
        while matrix != []:
            temp = []
            rows = len(matrix)
            if row:
                temp = matrix.pop(int(not row_rev) - 1)
                if row_rev: temp.reverse()
                res = res + temp
                row_rev = not row_rev
                row = False
            else:
                for i in range(0, rows):
                    temp.append(matrix[i].pop(int(col_rev) - 1))
                if col_rev: temp.reverse()
                res += temp
                col_rev = not col_rev
                if not matrix[0]:
                    break
                row = True
        return res
'''
[
[2,3,4],
[5,6,7],
[8,9,10],
[11,12,13],
[14,15,16]]
'''
            
                
            
