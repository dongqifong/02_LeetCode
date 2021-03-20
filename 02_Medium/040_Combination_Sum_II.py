'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
import os
os.system('clear')
class Solution:
    def combinationSum2(self, candidates, target):
        candidates=sorted(candidates)
        ans=[]
        self.dfs(candidates,target,[],ans)
        return ans
    def dfs(self,nums,target,path,ans):
        if target==0:
            ans.append(path)
        elif target<0:
            return None
        else:
            for i in range(len(nums)):
                if nums[i]==nums[i-1] and i>0:
                    continue#remove duplicate combination
                if nums[i]>target:
                    break#accelate-->no need to go farther if nums[i]>target
                self.dfs(nums[i+1:],target-nums[i],path+[nums[i]],ans)
        return None