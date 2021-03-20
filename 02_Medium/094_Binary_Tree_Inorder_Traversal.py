'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if root:
            self.inorder(root,res)
            return res
        else:
            return []
    def inorder(self,root,res):
        if root.left:
            self.inorder(root.left,res)   
        res.append(root.val)
        if root.right:
            self.inorder(root.right,res)

        
'''
inoder的順序是LDR
也就是先遍歷左子樹(root.left == None)
走到底後將val加入res
再往右子樹走
'''