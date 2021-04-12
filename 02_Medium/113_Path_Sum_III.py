'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return root
        else:
            res=[]
            self.dfs(root,targetSum-root.val,[root.val],res)
        return res
    def dfs(self,root,remain,path,res): 
    
        if not root.left and not root.right:
            if remain==0:
                res.append(path)
            return None
        else:
            if root.left:
                self.dfs(root.left,remain-root.left.val,path+[root.left.val],res)
            if root.right:
                self.dfs(root.right,remain-root.right.val,path+[root.right.val],res)
        return None

'''
典型的dfs題目，經過root以後，就從remain中扣除，並且把root加到path中，當走到left, right都為None時，表示到達葉節點

此時若remain為0，那這條路徑就是其中一個答案，加入res中
'''