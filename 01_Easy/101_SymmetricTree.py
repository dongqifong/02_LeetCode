import os
os.system('clear')

class TreeNode():
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def inorder(self):
        print(self.val)
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
class Solution:
    def isSymmetric(self, root):
        if root:
            return self.check(root.left,root.right)
        else:
            return True
    def check(self,L,R):
        if L and R:
            return L.val==R.val and self.check(L.left,R.right) and self.check(L.right,R.left)
        else:
            return L==R
            

       

print('--------------')
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(2)
t4=TreeNode(3)
t5=TreeNode(6)
t6=TreeNode(6)
t7=TreeNode(3)
t1.left=t2
t1.right=t3
t2.left=t4
t2.right=t5
t3.left=t6
t3.right=t7
#t1.inorder()
print('--------------')
s=Solution()
print(s.isSymmetric(t1))