import os
os.system('clear')

class Solution():
    def combine(self, n: int, k: int):
        remain=[i for i in range(1,n+1)]
        res=[]
        comb=[]
        self.dfs(remain,k,comb,res)
        return res
    def dfs(self,remain,k,comb,res):
        if k==0:
            res.append(comb)
        else:
            for i in range(len(remain)):
                self.dfs(remain[i+1:],k-1,comb+[remain[i]],res)
                if len(remain)-i-1<k:
                    return None
                
            
n=4
k=2
s=Solution()
ans=s.combine(n,k)
print(ans)
'''
當k!=0的時候
就把當前的index的數字加入組合comb裡面
當k==0時，就加入res結果裡面
再退回去找下一個
for裡面的
if len(remain)-i-1<k:
    return None
是提早跳出的條件
也就是剩下的數值數量少於k時
就不用再找下去了
因為全部都加進去還是小於k
'''
