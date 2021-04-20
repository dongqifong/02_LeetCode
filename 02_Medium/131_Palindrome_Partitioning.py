'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.dfs(s,[],res)
        return res
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
        len_s=len(s)
        for i in range(1,len_s+1):
            temp=s[0:i]
            if temp==temp[::-1]:
                self.dfs(s[i:],path+[s[0:i]],res)

'''
要得到所有的組合數，是典型的backtracking(dfs)，每次都取長度為i的substring
看看這個substring是不是回文，若是就是一個可能，那把這substring加到path中
剩下的字串進入下一次dfs
當s為空的時候，就是把s耗盡，把path加入res中
'''