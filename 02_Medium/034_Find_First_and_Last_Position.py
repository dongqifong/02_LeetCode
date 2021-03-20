'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
'''
class Solution:
    def searchRange(self, nums, target):
        left=0
        right=len(nums)-1
        if (not nums) or (nums[left]>target) or (nums[right]<target):
            return [-1,-1]
        while left<=right:
            if nums[left]==target and nums[right]==target:
                return [left,right]
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                while nums[left]<target:
                    left+=1
                while nums[right]>target:
                    right-=1
                return [left,right]
        return [-1,-1]