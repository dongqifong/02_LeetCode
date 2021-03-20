import os
os.system('clear')
class Solution:
    def climbStairs(self, n: int) -> int:
        stair=[1,1,2]
        for i in range(n+1):
            if i>len(stair)-1:
                stair.append(stair[i-1]+stair[i-2])
        return stair[n]

n=10
s=Solution()
print(s.climbStairs(n))