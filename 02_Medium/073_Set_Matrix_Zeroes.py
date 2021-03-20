'''
73. Set Matrix Zeroes
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
import os
os.system('clear')
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    self.turnsigh(matrix,i,j,m,n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='-1':
                    matrix[i][j]=0
        # for i in matrix:
        #     print(i)

    def turnsigh(self,matrix,r,c,m,n):
        for i in range(m):
            if matrix[i][c]!=0:
                matrix[i][c]='-1'
        for j in range(n):
            if matrix[r][j]!=0:
                matrix[r][j]='-1'

# matrix=[[1,1,1],[1,0,1],[1,1,1]]
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
s=Solution()
s.setZeroes(matrix)

'''
碰到0的時候把對應的十字位置用字串-1做標記(要用0.1也可以，不要是整數就好)
掃完以後把剛剛標記的字串再轉乘0
'''