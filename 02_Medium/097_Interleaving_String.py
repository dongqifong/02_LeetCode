import os
os.system('clear')
class Solution:
    def isInterleave(self, s1, s2, s3):
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        stack, visited = [(0, 0)], [(0, 0)]
        while stack:
            x, y = stack.pop()
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y)); visited.append((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1)); visited.append((x, y+1))
        return False
'''
每次比對s1[x]是否等於s3[x+y]以及s2[y]是否等於s3[x+y]
若有相同那麼就是有可能的搜尋點
把他加入stack和visisted
直到x+y==l代表找完了
'''
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s=Solution()
res=s.isInterleave(s1,s2,s3)
print(res)

