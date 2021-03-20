import os
os.system('clear')

class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0 for i in range(len(s)+1)]
        if s[0]!="0":
            dp[0:2]=[1,1]
        for i in range(2,len(s)+1):
            if 0<int(s[i-1:i])<10:
                dp[i]+=dp[i-1]
            if 10<=int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]

s=Solution()
res=s.numDecodings("122221")
print(res)
'''
將字串視為一個階梯
每一階都是前面兩階的組合總數(i-1,i-2)
但前一階必須要是在0<s[i-1:i]<10才有效
前兩階必須要在10<=s[i-1:i]<=26間才有效
最後return 最後一格
s_index:
  [0,1,2,3,4,5,6,7,8]
d_index:
[0,1,2,3,4,5,6,7,8,9]
所以d的長度要建成len(s)+1
'''