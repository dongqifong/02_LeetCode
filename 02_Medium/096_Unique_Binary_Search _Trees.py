class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return n
        else:
            # return self.helper1(1,n)
            return self.dp(n)
    #逐一走訪(參照上一題的想法，時間上不會過，因為n可以到19)
    def helper1(self,start,end):
        if start>end:
            comb=1
            return 1
        else:
            comb=0
            for i in range(start,end+1):
                leftcomb=self.helper1(start,i-1)
                rightcomb=self.helper1(i+1,end)
                comb+=leftcomb*rightcomb
        return comb
    
    def dp(self,n):
        g=[0]*(n+1)
        g[0]=1
        g[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                g[i]+=g[j-1]*g[i-j]
        return g[n]
'''

 Taking 1~n as root respectively:
       1 as root: # of trees = F(0) * F(n-1)  // F(0) == 1
       2 as root: # of trees = F(1) * F(n-2) 
       3 as root: # of trees = F(2) * F(n-3)
       ...
       n-1 as root: # of trees = F(n-2) * F(1)
       n as root:   # of trees = F(n-1) * F(0)
 
  So, the formulation is:
       F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
 
'''

n=8
s=Solution()
res=s.numTrees(n)
print(res)