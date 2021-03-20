'''
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
import os
os.system('clear')
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=list(num1)
        num2=list(num2)
        v1=0
        v2=0
        while num1 or num2:
            if num1:
                a=ord(num1.pop(0))-48
                v1=v1*10+a
            if num2:
                b=ord(num2.pop(0))-48
                v2=v2*10+b
            if v1==0 or v2==0:
                return str(0)
        return str(v1*v2)
num1='123'
num2='456'
s=Solution()
result=s.multiply(num1,num2)
print(result)