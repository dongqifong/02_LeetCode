'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] = min(dp[j],dp[j-coin]+1)
            print(dp)
        if dp[-1]==float("inf"):
            return -1
        else:
            return dp[-1]
    
'''
dp的第j個位置代表，組出總和為j的組合數
每次一種coin進來，如果他能組出j這個數字，
那他一定是從dp[j-coin]這個位置+coin來的
但是因為是要求最小組合
所以要改成，所以要同時比對還沒加coin前的組合數和+coin的組合數誰比較小
保留小的
直到把每一種coin都走一遍
時間複雜度len(coins)*len(amount)
空間複雜度len(amount)
'''