'''
47. Permutations II
Given a collection of numbers, nums,
that might contain duplicates, return all possible unique permutations in any order.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        path=[]
        # If length of nums<2:
        # The number of combination must be one.
        # return [nums]
        if len(nums)<2:
            return [nums]
        # Do DFS
        self.dfs(nums,path,ans)
        return ans
    def dfs(self,remain,path,ans):
        # The combination must be path+remain and path+reverse of remain
        if len(remain)==2:
            ans.append(path+remain)
            # if reverse of remain are not equal to remain, append this combination to ans
            if remain[::-1]!=remain:
                ans.append(path+remain[::-1])
        else:
            for i in range(len(remain)):
                # If i location is the same as last value,
                # Skip this index for avoiding duplicate combination
                if i>0 and remain[i]==remain[i-1]:
                    continue
                # candidate array=remain[0:i]+remain[i+1:]
                # path=previous path + remain[i]                    
                self.dfs(remain[0:i]+remain[i+1:],path+[remain[i]],ans)

'''
Based on last question(046_Permutation),
I add two process to exclude duplicate combination
if remain and reverse of remain are not equal to each other
append reverse of remain

'''