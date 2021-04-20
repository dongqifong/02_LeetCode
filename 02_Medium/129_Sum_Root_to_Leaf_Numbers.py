'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        return self.dfs(root,0)
        
    def dfs(self,root,path):
        path_left=0
        path_right=0
        if not root.left and not root.right:
            return 10*path+root.val
        if root.left:
            path_left=self.dfs(root.left,10*path+root.val)
        if root.right:
            path_right=+self.dfs(root.right,10*path+root.val)
        return path_left+path_right

'''
因為目標是從根(root)到某一支葉(leaf)的走訪結果，所以用dfs
因為是先處理root在分左右子樹，所以也用到前序(pre-order)排序的觀念(10*path+root.val)
也就是要往下走前，就要先把本身處理過(前面的紀錄*10+本身的值)
直到走到葉(leaf)為止
也可以把記錄存在一個array，但是這題只想知道最後加起來的值，所以不需要這樣，
分左右子樹的加總，再合起來就好了
'''