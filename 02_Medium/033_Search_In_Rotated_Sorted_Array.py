'''
33. Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<right and (nums[left]<=target or nums[right]>=target):
            if nums[left]==target:
                return left
            else:
                left+=1
                
            if nums[right]==target:
                return right
            else:
                right-=1
        if nums[left]==target:
            return left
        else:
            return -1