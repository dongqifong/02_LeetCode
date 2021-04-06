'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal
 of a binary tree and inorder is the inorder traversal of the same tree, 
 construct and return the binary tree.

'''

import os
os.system("clear")
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
 
'''
preorder的順序是parent-left-right
所以第一個element代表了根節點

接下來找他的左子樹和右子樹
這時找根節點在inorder中的位置
則inorder的左半部就是左子樹;右半部就是右子數

當inorder變成空(empty)，代表沒有子節點了
return None

remark:因為每次會把preorder第0個element移除掉，且preorder的順序是parent-left-right，所以一定是要先接左節點再接右節點

'''