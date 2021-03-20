
'''
Given a string s containing only digits, 
return all possible valid IP addresses that can be obtained from s. 
You can return them in any order.

A valid IP address consists of exactly four integers, 
each integer is between 0 and 255, separated by single dots and cannot have leading zeros. 
For example, 
"0.1.2.201" and "192.168.1.1" are valid IP addresses and 
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
'''
import os
os.system('clear')

class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s)<4 or int(s)>255255255255:
            return []
        else:
            res=[]
            self.dfs(remaining=s,level=0,path="",res=res)
            return res
    def dfs(self,remaining,level,path,res):
        if level==4:
            if remaining=="":
                res.append(path)
            return
        for i in range(1,3+1):
            if len(remaining)<i:
                return
            if i>1 and remaining[0]=="0":
                continue
            else:
                if 0<=int(remaining[0:i])<=255:
                    if level>0:
                        self.dfs(remaining[i::],level+1,path+"."+remaining[0:i],res)
                    else:
                        self.dfs(remaining[i::],level+1,remaining[0:i],res)
                else:
                    continue

S=Solution()
s="101023"
res=S.restoreIpAddresses(s)
print(res)

'''
定義ip由左到右為level1~4
用DFS去走訪每一個level
每一個level都可以擺1~3個數字(用for去走訪)
但是要在0~255之間，否則就continue，不用再續往下走
除此之外，如果remaing的長度小於當前需要取的長度，那也不需要往下走
當level到達4且有把remaing用盡(remaing==")表示合法
把這個path加入res中
'''