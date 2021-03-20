'''
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

'''
import os
import numpy as np
os.system('clear')

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp_map=[[0]*n for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]!=1:
                dp_map[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]!=1:
                dp_map[0][j]=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    dp_map[i][j]=dp_map[i-1][j]+dp_map[i][j-1]
        return dp_map[-1][-1]
m=9
n=9
test_case=np.random.choice([0,0,0,0,0,0,0,0,1],m*n).reshape(m,n)
test_case[-1][-1]=0
test_case[0][0]=0
print(test_case.tolist())
s=Solution()
res=s.uniquePathsWithObstacles(test_case)
print(res)

'''
和062觀念一樣，但是因為有障礙物，沒辦法直接靠直接計算，只能用dp
額外創建一個地圖dp_map，每一格都先設成0
接著沿著dp_map的最左側和最上側邊走訪
若沒碰到障礙物就設成1，因為表示這是同一條路
若碰到了，就跳出
之後就和上一題一樣
每一個非障礙物的點的總步數，都是左側和上側加起來
最後return dp_map[-1][-1]
'''