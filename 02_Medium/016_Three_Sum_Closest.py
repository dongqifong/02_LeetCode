'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum=999999
        nums.sort()
        l=len(nums)-1
        for i in range(len(nums)-1):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                diff=s-target
                if abs(diff)<abs(min_sum-target):
                    min_sum=nums[i]+nums[l]+nums[r]
                    print(i,l,r)
                if diff<0:
                    l+=1
                elif diff>0:
                    r-=1
                else:
                    return target
        return min_sum
