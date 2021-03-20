'''
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

import os
os.system('clear')
class Solution:
    def generateMatrix(self, n: int):
        ans=[[0]*n for i in range(n)]
        start_row=0
        start_col=0
        end_row=n-1
        end_col=n-1
        iters=1
        while n>0:
            #go right
            for j in range(start_col,end_col+1,1):
                ans[start_row][j]=iters
                iters+=1
            start_row+=1
            #go down
            for i in range(start_row,end_row+1,1):
                ans[i][end_col]=iters
                iters+=1
            end_col-=1
            #go left
            for j in range(end_col,start_col-1,-1):
                ans[end_row][j]=iters
                iters+=1
            end_row-=1
            #go right
            for i in range(end_row,start_row-1,-1):
                ans[i][start_col]=iters
                iters+=1
            start_col+=1
            n-=2
        if n>0:
            ans[end_row][start_col]=iters
        return ans
n=4
s=Solution()
res=s.generateMatrix(n)
print(res)

#作法跟054觀念一樣，而且因為是正方形的形狀，離外情況只有n是奇數的情況
#主要觀念還是
#向右填值會使得start_row+1
#向下填值會使得end_col-1
#向左填值會使得end_row-1
#向上填值會使得start_col+1
#接著注意for的邊界
