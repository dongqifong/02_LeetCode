'''
Given the root of a binary tree, 
return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''

import os
os.system('clear')


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res=[]
        que=[root]
        level=0
        self.bfs(que,level,res)
        return res
    def bfs(self,que,level,res):
        if not que:
            return None
        res.append([])
        for i in range(len(que)):
            node=que.pop(0)
            res[level].append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        if level%2==1:
            res[level]=res[level][::-1]
        self.bfs(que,level+1,res)


'''
題目是一層一層的走訪，所以也是以bfs的方法逐一走訪每個節點和把左節點右節點加入que
但因為是zigzag排列方法，在level%2==1的地方，要把res[level]的順序倒過來
(再繼續往下走，不需要動que的順序)
'''