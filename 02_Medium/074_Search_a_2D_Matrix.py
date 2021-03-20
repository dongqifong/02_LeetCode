'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
import os
os.system('clear')
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if matrix[0][0]>target:
            return False
        ans=False
        col_0=[matrix[i][0] for i in range(len(matrix))]
        start=self.binary_search_start(col_0,target)
        res=self.binary_search_end(matrix[start],target)
        return res
    def binary_search_start(self,array,target):
        left=0
        right=len(array)-1
        #若target大於array[right]
        #提早結束，因為一定要回傳right
        if array[right]<=target:
            return right
        #尋找區間
        while right-left>1:
            m=(left+right)//2
            if array[m]<target:
                left=m
            elif array[m]>target:
                right=m
            else:
                return m
        return left
    def binary_search_end(self,array,target):
        left=0
        right=len(array)-1
        while left<=right:
            m=(left+right)//2
            if array[m]<target:
                left=m+1
            elif array[m]>target:
                right=m-1
            else:
                return True
        return False
        
            
        

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=12
s=Solution()
res=s.searchMatrix(matrix,target)
print(res)

'''
第一種解法
用兩次二分搜尋法
第一次找應該從哪一個row開始
也就是target要在left和right之間
而且right-target>1就要一直搜尋

第二次二分搜尋法用在從某個row開始向右搜尋
若找得到的話就return True
否則return False


第二種解法
因為上一個row的最後一個數字也小於當前row的第一個數字
所以可以把它當成一個1-D的陣列
用二分搜尋法一次就可以找完了
方法是設計個變數為m*n-1
left=0
right=m*n-1
m=(left+right)//2
然後把left,right,m換算成row和col去比較
假設num=left
則left對應的row和col如下換算
row=(m*n-1)//num
col=(m*n-1)%num
之後也是如同binary_search_end的方法
'''