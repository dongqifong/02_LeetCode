import os
os.system('cls')

class Solution:
    def reverse(self, x: int) -> int:
        result=0
        sign=1
        if x<0:
            sign=-1
            x=-x
        while x:
            result=result*10+x%10
            x=x//10
        result=sign*result
        if result>(2**31-1) or result<(-2**31):
            return 0
        return result

x=1234567
result=Solution()
print(result.reverse(x))

