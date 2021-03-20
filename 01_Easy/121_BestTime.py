'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
import os 

try:
    os.system('clear')
finally:
    os.system('cls')


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            profit=max(prices[i]-buy,profit)
            if prices[i]<buy:
                buy=prices[i]
        return profit




#prices=[1,4,2]
#prices=[2,1,2,1,0,0,1]
prices=[7,1,5,3,6,4]
s=Solution()
print('Max Profit=',s.maxProfit(prices))