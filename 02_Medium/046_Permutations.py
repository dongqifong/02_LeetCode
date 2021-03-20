'''
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        #the combination must be path+remain and path+reverse of remain
        if len(remain)==2:
            ans.append(path+remain)
            ans.append(path+remain[::-1])
        else:
            for i in range(len(remain)):
                # candidate array=remain[0:i]+remain[i+1:]
                # path=previous path + remain[i]
                self.dfs(remain[0:i]+remain[i+1:],path+[remain[i]],ans)
'''
Use deep first search(DFS) method
For each step, we append remain[i] into path, and use remain[0:i]+remain[i+1:] to do next step
When the lenth of remain is equal to 2, the combination must be path+remain and path+remain[::-1]


For example1([1,2,3]),

First iteration
[1,2,3]
remain=[2,3],path=[1]
the combination must be [1]+[2,3] and [1]+[3,2]

next iteration
remain=[2], path=[1,3]
the combination must be [2]+[1,3] and [2]+[3,1]

next iteration
remain=[3], paht=[1,2]
the combination must be [3]+[1,2] and [3]+[2,1]



For example2([1,2,3,4]),
First iteration
[1,2,3,4]
remain=[2,3,4],path=[1]
because length of remain>2-->do dfs
remain=[3,4],path=[1,2]
when length of remain is equal to 2
the combination must be [1,2]+[3,4] and [1,2]+[4,3]

go back to previous step
remain=[1,3,4],path=[2]
remain=[3,4],paht=[2,1]
the combination must be [2,1]+[3,4] and [2,1]+[4,3]
.
.
.

'''