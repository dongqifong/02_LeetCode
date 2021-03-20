import os
os.system('clear')

class Solution:
    def subsetsWithDup(self, nums):
        nums=sorted(nums)
        res=[[]]
        # go through 1~k combinations from nums
        for k in range(1,len(nums)+1):
            temp=[]
            self.combination(nums,temp=temp,res=res,k=k)
        return res

    # choose k values from nums2
    def combination(self,nums2,temp,res,k):
        if k==0:
            res.append(temp)
        else:
            n=len(nums2)
            i=0
            while i<n:
                self.combination(nums2[i+1:],temp+[nums2[i]],res,k-1) 

                # skip duplicated location
                while i+1<n and nums2[i+1]==nums2[i]:
                    i+=1
                # do next combination
                i+=1

nums=[1,2,2,3,4]
s=Solution()
res=s.subsetsWithDup(nums)
print(res)
