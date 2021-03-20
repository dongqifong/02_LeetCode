'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

'''
class Solution:
    def divide(self, dividend, divisor):
        sign=1
        if (dividend<0)^(divisor<0):
            sign=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=0
        while divisor<=dividend:
            temp=divisor
            mul=1
            while dividend>=temp<<1:
                temp<<=1
                mul<<=1
            res+=mul
            dividend-=temp
        res=sign*res
        if res>2**31-1:
            return 2**31-1
        if res<-2**31:
            return -2**31
        return res


s =Solution()
res=s.divide(-500,3)
print(res)
