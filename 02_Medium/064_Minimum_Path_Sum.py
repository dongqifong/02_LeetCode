'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid) -> int:
        m=len(grid)
        n=len(grid[0])
        for row in range(1,m):
            grid[row][0]+=grid[row-1][0]
        for col in range(1,n):
            grid[0][col]+=grid[0][col-1]
        #For each grid[i][j], the mimum steps is min(grid[i-1][j],grid[i][j-1])+itself
        #This is DP proplem
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
            

'''
每一格的最佳步數，都是左邊或上面比較小的值加到本身
逐一走到終點，回穿grid[-1][-1]
就是最短路徑了
'''