import os
os.system('cls')
class Solution:
    #solution 1
    def twoSum(self, nums, target):
        seen={}
        for i,v in enumerate(nums):
            remaining=target-v
            if remaining not in seen:
                seen[v]=i
            else:
                return [seen[remaining],i]
        return []
    #solution 2
    def twoSum2(self,nums,target):
        for i in range(len(nums)):
            remaining=target-nums[i]
            scan=nums[i+1::]
            if remaining in scan:
                return [i,scan.index(remaining)+i+1]
        return []
s=Solution()
nums=[3,3]
target=6
print(s.twoSum(nums,target))
print(s.twoSum2(nums,target))