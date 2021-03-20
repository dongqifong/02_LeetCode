import os
os.system('cls')
class Solution:
    #use combination method
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        total=m+n-2
        m_1=1
        n_1=1
        y=1
        
        for i in range(1,total+1):
            y=y*i
            if i==m-1:
                m_1=y
            if i==n-1:
                n_1=y
        m_n=y
        return int(m_n/(m_1*n_1))
    #the same as above method
    #just use a array to record exsist value of factorial
    def uniquePaths1_1(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        total=m+n-2
        y=[1]*total
        for i in range(1,total):
            y[i]=y[i-1]*(i+1)
        return int(y[-1]/(y[m-1-1]*y[n-1-1]))
    
    #DP method
    def uniquePaths_DP(self, m: int, n: int) -> int:
        aux = [[1]*n for x in range(m)]
        # print(aux)
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]

print('--------------------------------------------------------------')
m=5
n=23
s=Solution()
res1=s.uniquePaths(m,n)
res1_2=s.uniquePaths1_1(m,n)
res2=s.uniquePaths_DP(m,n)
print(res1,res1_2,res2)

'''
這題不能用dfs或bfs
要用DP或是排列的算法
要到達目的地一定是往下走m-1次且向右走n-1次
所以走法就是(m-1)+(n-1)個位置中隨便排列
假設m=3,n=4
向下走的動作表示為D，向右走表示為R
所以到達目的地一定是DDRRR這五個符號的排列組合
所以是(m+n-2)!/((m-1)!*(n-1)!)
'''