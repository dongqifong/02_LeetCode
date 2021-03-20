import os
os.system('cls')
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left=0
        right=len(nums)
        mid=(left+right)//2
        while left<right:
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid
            else:
                return mid
            mid=(left+right)//2
        return mid
    # def searchInsert(self, nums, target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         l=0
    #         r=len(nums)-1
    #         m=(l+r)//2
    #         if target<=nums[l]:
    #             return l
    #         if target==nums[r]:
    #             return r
    #         if target>nums[r]:
    #             return r+1
    #         while r-l>1:
    #             if target<nums[m]:
    #                 r=m
    #                 m=(l+r)//2
    #             elif target>nums[m]:
    #                 l=m
    #                 m=(l+r)//2
    #             else:
    #                 return m
    #         return m+1

nums=[1,3,5,6]
target=7
s=Solution()
result=s.searchInsert(nums,target)
print(result)