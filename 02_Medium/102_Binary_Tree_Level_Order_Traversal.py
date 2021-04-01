'''
Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., 
from left to right, level by level).
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
    def levelOrder(self, root: TreeNode):
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
        self.bfs(que,level+1,res)
        return None


'''
因為題目要求一層一層輸出，這種題目就是用廣度優先搜尋
到某一層後，用for走過每個節點，並把每一個節點左節點和右節點，都依序加入佇列
該層走完後，就往下一層走
直到佇列為空
'''