'''
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

import os
os.system('clear')
class Solution:
    def spiralOrder(self, matrix):
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            #上方走完，row_begin向內縮
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            #右方向下走完，col_end向內縮
            col_end -= 1

            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                #下方走完，row_end向內縮
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                #左方走完，col_begin向內縮
                col_begin += 1
        return res

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
res=s.spiralOrder(matrix)
print(res)