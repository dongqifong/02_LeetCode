import os
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

'''
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        End=len(nums)-1
        while i>0:
            if nums[i]>nums[i-1]:
                k=self.find_next_larger_index(nums,t=nums[i-1])
                nums[i-1],nums[k]=nums[k],nums[i-1]
                self.reverse(nums,i,End)
                return
            i-=1
            if i==0:
                self.reverse(nums,0,End)
                return
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return None
    def find_next_larger_index(self,nums,t):
        k=len(nums)-1
        while k>0:
            if nums[k]>t:
                return k
            k-=1
        return None