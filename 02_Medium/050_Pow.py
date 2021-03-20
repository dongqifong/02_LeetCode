'''
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x,-n)
        else:
            #2^100=(2^50)*(2^50)
            #half=2^50
            half=self.myPow(x,n//2)
            #if n is even:
            #result=half*half
            if n%2==0:
                return half*half
            #if n is odd
            #result=half*half*x
            #e.g.
            #2^99=(2^49)*(2^49)*(2)
            else:
                return half*half*x

