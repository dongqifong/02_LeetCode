import os
os.system('clear')

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            temp=(digits[i]+1)//10
            digits[i]=(digits[i]+1)%10
            if temp==0:
                return digits
        if digits[0]==0:
            return [1]+digits

digits=[4,0,0,9]
s=Solution()
result=s.plusOne(digits)
print(result)