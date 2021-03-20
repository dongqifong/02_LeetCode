import os
import numpy as np
os.system('clear')

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isBalanced(self,root):
        if root is None:
            return True
        return abs(self.height(root.left)-self.height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
   
    def height(self,root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left),self.height(root.right))+1
        
v1=TreeNode(1)
v2=TreeNode(2)
v3=TreeNode(2)
v4=TreeNode(3)
v5=TreeNode(3)
v6=TreeNode(4)
v7=TreeNode(4)
v1.left=v2
v1.right=v3
v2.left=v4
v2.right=v5
v4.left=v6
v4.right=v7
# v3.left=TreeNode(None)
# v3.right=TreeNode(None)


s=Solution()
result=s.isBalanced(v1)
print(result)

