'''
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
'''

class Solution:
    def change(self, amount, coins) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j]+=dp[j-coin]
        return dp[-1]  


'''
dp[amount]代表最終能組出amount這個數字的組合數
dp[0]代表什麼都不做的初始狀態
dp[j]代表組出j到目前出現的coin能組出來的組合數
所以，若第j個位置可以由數值為coin組合出來，那他一定是從dp[j-coin]
加過來的
把所有coin組合加一遍，return 最後一格位置就是組合成amount這個數字的組合數
'''