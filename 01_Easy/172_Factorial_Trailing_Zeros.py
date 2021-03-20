'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result=0
        while n!=0:
            result+=n//5#calculate the number of 5 in 1~n
            n=n//5#exclude the combination(5,2)
        return result

