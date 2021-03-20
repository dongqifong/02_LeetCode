'''
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums) -> int:
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        #faster than putting judge process after each process of "seen[i]+=1"
        #because the length of seen is shorter than nums
        for i in seen:
            if seen[i]>len(nums)//2:
                return i