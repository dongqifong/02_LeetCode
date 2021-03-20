import os
import math
os.system('clear')
class solution():
    def getRow(self,rowIndex:int):#faster
        if rowIndex==0:
            return [1]
        d=[]
        iters=(rowIndex+1)/2
        for i in range(int(math.ceil(iters))):
            d.append(self.choice(rowIndex,rowIndex-i))
        if (rowIndex+1)%2!=0:
            for i in range(len(d)-2,-1,-1):
                d.append(d[i])  
            return d
        else:
            for i in range(len(d)-1,-1,-1):
                d.append(d[i])
            return d
    def getRow2(self,rowIndex:int):#slower
        if rowIndex==0:
            return [1]
        d=[]
        for i in range(rowIndex+1):
            d.append(self.choice(rowIndex,rowIndex-i))
        return d
    def choice(self,a,b):
        return int(self.factorial(a)/(self.factorial(b)*self.factorial(a-b)))
    def factorial(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.factorial(n-1)
s=solution()
rowIndex=5
print(s.getRow(rowIndex))
print(s.getRow2(rowIndex))
