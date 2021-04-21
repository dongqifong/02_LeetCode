'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]
        return dp[-1]

'''
dp第0個位置什麼都不做的情況設為True

dp[i]個位置代表從s[0:i]子字串
若這個子字串的尾部是wordDict內的任一個字，那他一定是從位置i-len(word)向下拼的
所以dp[i]的結果就是dp[i] or dp[i-len(word)]

例如
s="acd"
wordDict=["a","cd"]
dp=[True,False,False,False]

當i=1時dp[1]會改為True
原因是他是以“什麼都不接的情況”從頭找1個子字串，而且這個子字串的結尾有在wordDict裡面
所以dp[1]=dp[1] or dp[1-len("a")]
也就是dp[1]=dp[1] or dp[0]

之後到i=3時
dp[3]=dp[3] or dp[3-len("cd")]
也就是dp[3]=dp[3] or dp[1]
這個位置結尾能夠在字典裡找到
那他一定是從dp[i-len(substring in dict)]來的
'''