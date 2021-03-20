import os
os.system('clear')

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class solution():
    def sortedArrayToBST(self, nums):
        left=0
        right=len(nums)-1
        return self.buildBST(left,right,nums)

    def buildBST(self,l,r,nums):
        m=l+(r-l)//2        
        if l>r:
            return None
        root=TreeNode(nums[m])
        print(root.val)
        root.left=self.buildBST(l,m-1,nums)
        root.right=self.buildBST(m+1,r,nums)
        return root

mylist=[-10,-3,0,5,9]
s=solution()
result=s.sortedArrayToBST(mylist)
print(1//2)
