
import os
os.system('clear')
class Solution:
    def removeDuplicates(self, nums) -> int:
        i=0
        for n in nums:
            if i<2 or n>nums[i-2]:
                nums[i]=n
                i+=1
        return i
'''
主要分兩個判斷式
前兩個(i=0 and i=1)因為肯定能存在於陣列
但是當i>=2時
每個位置的值只要大於i-2位置的數值才可以存在於數列
若為等於表示重複至少三次，要skip掉
最後return i
'''