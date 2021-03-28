# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        # Method 1: broadcast min and max value to next level
        return self.passMinMax(root)

        # Method 2: use inorder sort and check whether output list is asc.
        # res=[]
        # self.inorder(root,res)
        # print(res)
        # for i in range(len(res)-1):
        #     if res[i]>=res[i+1]:
        #         return False
        # return True
        
    def passMinMax(self,root,Min = float('inf'), Max = float('-inf')):
        if not root:
            return True
        if root.val <= Max or root.val >= Min:
            return False
        return self.passMinMax(root.left, min(Min, root.val), Max) and \
               self.passMinMax(root.right, Min, max(root.val, Max))  
            

    def inorder(self,root,res):
        if root.left:
            self.inorder(root.left,res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right,res)

'''
第一種方法是傳遞最大最小值下去

第二種方法是用中序搜尋，因為如果是正確的BST，那搜尋完應該要由小到大排列

'''