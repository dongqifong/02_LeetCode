import os
os.system('clear')

class Tree():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
v1=Tree(3)
v2=Tree(9)
v3=Tree(20)
v4=Tree(15)
v5=Tree(7)
v6=Tree(8)
v7=Tree(9)
v8=Tree(10)
v9=Tree(11)



v1.left=v2
v1.right=v3
v3.left=v4
v3.right=v5
v4.left=v6
v4.right=v7
v5.left=v8
v5.right=v9
class Solution:
    def levelOrderBottom(self, root):
        from collections import deque
        if root is None:
            return []
        level = 0
        levels = []
        q = deque()
        q.append(root)
        
        while q:
            level_len = len(q)
            levels.append([])
            for item in range(level_len):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels[::-1]

s=Solution()
ans=s.levelOrderBottom(v1)
print(ans)