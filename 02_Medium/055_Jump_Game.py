'''
55. Jump Game
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''
class Solution:
    def canJump(self, nums) -> bool:
        #Calculate length of nums
        L=len(nums)
        
        #if length of nums equal to 1, it must be true.
        if L==1:
            return True
        #initialize the max step
        max_step=1
        #Compare max_step-1 with nums[i]
        #if nums[i]>max_step, update max_step
        #if max_step is under or equal to 0, stuck at this position.
        for i in range(L):
            #len(nums[i:]-1)
            L-=1
            max_step=max(max_step-1,nums[i])
            if max_step<=0:
                return False
            #if max_step is larger or equal nums[i:]-1, it must be able to jump to last index
            elif max_step>=L:
                return True
        return False
    
#就是一直搜尋往下找跟跳到下一格哪個可以走比較遠
#當能夠走的距離歸零了
#就return False
#若沿途能找到一格，使得這個長度>=該格"之後(num[i:]-1)"的長度
#就return True