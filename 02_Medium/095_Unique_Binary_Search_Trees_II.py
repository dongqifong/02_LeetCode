import os
os.system("clear")
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n==1:
            return [TreeNode(n)]
        else:
            return self.helper(1,n)
    def helper(self,start,end):
        TreeList=[]
        if start>end:
            TreeList.append(None)
        else:
            for i in range(start,end+1):
                LeftList=self.helper(start,i-1)
                RightList=self.helper(i+1,end)
                for L in LeftList:
                    for R in RightList:
                        root=TreeNode(i)
                        root.left=L
                        root.right=R
                        TreeList.append(root)
        return TreeList
'''
Binary Search Tree的左節點小於root，右節點大於root
用for逐一走訪把i當成root
那start~ i-1的BST就要接在左邊
i+1~ end的BST要接在右邊
左邊的子樹按照同樣想法向下接
當start>end的時候就代表要停止了(比方說i=1時，左邊要接helper(1,1-1)的回傳值，也就是None)
加入None
把每一個root的左子樹和右子樹的組和接完後就可已回傳TreeList了
'''
n=5
s=Solution()
res=s.generateTrees(n)
for head in res:
    # temp=head
    q=[]
    v=[]
    q.append(head)
    v.append(head.val)
    while q:
        temp=q.pop(0)
        if temp.left:
            q.append(temp.left)
            v.append(temp.left.val)
        if temp.right:
            q.append(temp.right)
            v.append(temp.right.val)
    print(v)
    print("-"*25)
            
    