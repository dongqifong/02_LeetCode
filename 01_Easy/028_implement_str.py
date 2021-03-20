import os
os.system('cls')
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle=len(needle)
        start=0
        while start<len(haystack)-len_needle+1:
            print(haystack[start:start+len_needle])
            if haystack[start:start+len_needle]==needle:
                return start
            start+=1
        return -1
haystack='hello'
needle='ll'
s=Solution()
result=s.strStr(haystack,needle)
print(result)