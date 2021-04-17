'''
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottim-up method
        res=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j]=triangle[i][j]+min(res[j],res[j+1])
        return res[0]

'''
用dp的方法
從底層開始
res[j]的更新，一定是從上一層的triangle[i][j]和res[j],res[j+1]來的
最小值會被一路洗到res的最左邊，因為內層的for是跟著triangle[i]的element數目走的
最後return res[0]
'''