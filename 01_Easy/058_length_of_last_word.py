import os
os.system('clear')
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip(" ").split(" ")
        return len(s[-1])

string="a "
s=Solution()
result=s.lengthOfLastWord(string)
print(result)