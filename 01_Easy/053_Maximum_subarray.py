import os
os.system('clear')
test=[-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)


s=Solution()
result=s.maxSubArray(test)
print(result)