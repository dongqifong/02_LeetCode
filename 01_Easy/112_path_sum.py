import os
os.system('clear')
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution():
    def hasPathSum(self,root,sum)->bool:
        if root:
            if not root.left and not root.right:
                if sum-root.val!=0:
                    return False
                else:
                    return True
            return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        else:
            return False


        

v1=TreeNode(1)
v2=TreeNode(2)
v3=TreeNode(3)
v4=TreeNode(4)
v5=TreeNode(5)
v6=TreeNode(6)

# v1.left=v2
# v1.right=v3
# v2.left=v4
# v3.left=v5
# v3.right=v6
v1.left=v2
v2.left=v3
v3.left=v4
v4.left=v5

sum=15
s=solution()
print(s.hasPathSum(v1,sum))