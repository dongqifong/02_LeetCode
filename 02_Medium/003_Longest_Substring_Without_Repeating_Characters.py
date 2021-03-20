'''
Given a string s, find the length of the longest substring without repeating characters.
'''
from os import system
system('clear')

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen={}
        max_len=0
        start=0
        for i, ch in enumerate(s):
            if ch in seen:
                max_len = max(max_len, i-start) # update the res
                start = max(start,seen[ch]+1)  # here should be careful, like "abba"
            seen[ch] = i
        return max(max_len, len(s)-start)  # return should consider the last non-repeated substring


test='abba'
s=Solution()
s.lengthOfLongestSubstring2(test)