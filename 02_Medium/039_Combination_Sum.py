'''
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
'''
from os import system
system('clear')
class Solution:
    def combinationSum(self, candidates, target):
        ans=[]
        self.dfs(candidates,target,candidates[0],ans)
        return ans
    
    def dfs(self, nums, target, path, ans):
        if target==0:
            ans.append(path)
        elif target<0:
            return None
        else:
            for i in range(len(nums)):
                self.dfs(nums[i:],target-nums[i],path+[nums[i]],ans)
        return None

candidates=[2,3,6,7]
target=7
s=Solution()
result=s.combinationSum(candidates,target)
print(result)
    
        
            