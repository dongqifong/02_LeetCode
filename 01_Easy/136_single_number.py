'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?


'''
import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

class Solution:
    def singleNumber(self, nums):
        result=0
        print(result)
        for i in range(len(nums)):
            result^=nums[i]
            print(result)
        return result
nums=[2,100,2,100]
s=Solution()
r=s.singleNumber(nums)
print(r)