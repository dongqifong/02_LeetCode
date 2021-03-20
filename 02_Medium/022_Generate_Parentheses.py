import os
os.system('clear')
class Solution:
    def generateParenthesis(self, n: int):
        last_list=[]
        last_list.append("()")
        k=1
        self.insert(last_list,k+1,n)
        return last_list
    def insert(self,last_list,k,n):
        if k>n:
            return None
        list_len=len(last_list)
        for i in range(list_len):
            temp=last_list.pop(0)
            temp_len=len(temp)
            for j in range(1,temp_len):
                s=temp[0:j]+"()"+temp[j::]
                if not s in last_list:
                    last_list.append(s)
            s=temp[0:temp_len]+"()"
            if not s in last_list:
                last_list.append(s)
        #print(last_list)
        self.insert(last_list,k+1,n)
    def generateParenthesis2(self, n):
        dp = [[] for i in range(n + 1)]
        print('init dp=',dp)
        dp[0].append('')
        print('append=',dp)
        for i in range(n + 1):
            for j in range(i):
                print((i,j))
                temp=['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                dp[i] += temp
                print(temp)
        return dp[n]
    def generateParenthesis3(self,n):
        ans=[]
        def backtrack(s="",left=0,right=0):
            if len(s)==2*n:
                ans.append(s)
            else:
                if left<n:
                    backtrack(s+"(",left+1,right)
                if left>right:
                    backtrack(s+")",left,right+1)
        backtrack("",left=0,right=0)
        return ans

s=Solution()
n=4
result=s.generateParenthesis3(n)
print(result)