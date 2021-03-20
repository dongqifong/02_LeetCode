import os
if os.name=='nt':#windows
    os.system('cls')
else:
    os.system('clear')
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:return ""
        s_min=min(strs)
        s_max=max(strs)
        print(s_min)
        print(s_max)
        for i,v in enumerate(s_min):
            if v!=s_max[i]:
                return s_min[:i]
        return s_min

test=["dogcar","racecar","car"]
s=Solution()
r=s.longestCommonPrefix(test)
print(r)