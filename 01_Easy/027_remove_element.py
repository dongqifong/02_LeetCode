import os
os.system('cls')
class Solution:
    def removeElement(self, nums, val) -> int:
        j=0
        L=len(nums)
        for i in range(0,L):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
        # return nums[0:j]
        return j
nums=[3,2,2,3]
val=3
s=Solution()
result=s.removeElement(nums,val)
print(result)
print(nums)