'''
41. First Missing Positive
Given an unsorted integer array nums, find the smallest missing positive integer.
'''
import os
os.system('clear')
class Solution:
    def firstMissingPositive(self, nums):
        print('original array=',nums)
        print('original lengh of array=',len(nums))
        print()
        nums.append(0)
        n=len(nums)
        for i in range(n):
            if nums[i]<0 or nums[i]>n-1:
                nums[i]=0
        print('shift useless element to 0')
        print(nums)
        print()
        for i in range(n):
            index=nums[i]%n
            nums[index]=nums[index]+n
        #change finding value to index 1~n-1
        #set this inex larger than n
        #so that the first index of value<n is the first missing positive value
        print('transfer seen value to index and set this index larger than length of nums')
        print(nums)
        print()
        #if nums[i]<n where i=1~n-1
        #this position is the missing value
        for i in range(1,n):
            if nums[i]//n==0:
                return i
        return n

testcase=[0,1,2,4,7,7,7,100]
#length=8
#miss "3"
s=Solution()
res=s.firstMissingPositive(testcase)
print(res)