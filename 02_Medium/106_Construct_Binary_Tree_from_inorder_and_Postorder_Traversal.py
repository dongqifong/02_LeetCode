'''
Given two integer arrays inorder and postorder 
where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and 
return the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map_inorder={}
        for i,v in enumerate(inorder):
            map_inorder[v]=i
        def build(low,high):
            if low>high:
                return None
            root=TreeNode(postorder.pop())
            root_loc=map_inorder[root.val]
            root.right=build(root_loc+1,high)            
            root.left=build(low,root_loc-1)
            return root
        return build(0,len(inorder)-1)
        

'''
postorder的順序是left-right-parent

所以最後面的就是根節點

接著找他在inorder中的位置

他的左半部就是左子樹

右半部就是右子樹

但因為postorder順序和每次都會把postorder的最後一個元素pop掉(所以馬上碰到的會是右子樹)，所以一定要先接右子樹再接左子樹

'''