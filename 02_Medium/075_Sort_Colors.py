'''
75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.


'''
import os
os.system('clear')
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change=len(nums)
        for i in range(1,3):
            j=0
            while j<change:
                if nums[j]==i:
                    nums.append(nums.pop(j))
                    change-=1
                else:
                    j+=1


nums=[2,0,2,1,1,0]
s=Solution()
s.sortColors(nums)
'''
逐一走否整個數列
若碰到1就把他pop掉
再append到後面
每pop一次都代表要搜尋的範圍會少一

第二次走訪是看到2就把他pop掉
再append到後面

這樣一定就是0擺前面
2擺最後面
1在中間

本質上跟泡沫排序法有點像
只是由小到大逐一看
排完的就不用理他了

如果可以額外宣告一個陣列
那可以用快速排序法會更快
但是題目說要用in-place
'''