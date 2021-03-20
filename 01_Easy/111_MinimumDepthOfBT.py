import os
os.system('clear')

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=ValueError
        self.left=left
        self.right=right
class Solution():
    def minDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.bfs(root)

    def bfs(self, root) -> int:
        from collections import deque
        q=deque()
        level=1
        q.append(root)
        while q:
            q_len=len(q)
            for i in range(q_len):
                n=q.popleft()
                if not n.left and not n.right:
                    return level
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level+=1
        return level
                

