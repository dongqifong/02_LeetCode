import os
os.system('cls')

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

test_list=[1,1,2]
s=Solution()
result=s.removeDuplicates(test_list)
print(result)
print(test_list[0:result])