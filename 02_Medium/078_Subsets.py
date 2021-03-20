import os
os.system('clear')


class Solution:
    def subsets(self, nums):
        res=[[]]
        for level in range(1,len(nums)+1):
            comb=[]
            self.dfs(nums,level,comb,res)
        return res

    def dfs(self,remain,k,comb,res):
        if k==0:
            res.append(comb)
        else:
            for i in range(len(remain)):
                self.dfs(remain[i+1:],k-1,comb+[remain[i]],res)
                if len(remain)-i-1<k:
                    return None

        

nums=[1,2,3]
s=Solution()
res=s.subsets(nums)
print(res)

'''
借用上一題(077)
只是在subsets方法中
多用一層for逐一跑指定長度的組合
'''