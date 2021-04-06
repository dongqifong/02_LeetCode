'''
Given the root of a binary tree, 
return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        else:
            q=[]
            q.append(root)
            
            level=0
            levels=[]
            while q:
                len_q=len(q)
                levels.append([])
                for i in range(len_q):
                    node=q.pop(0)
                    levels[level].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level+=1
            return levels[::-1]


'''
想法就是從上往下，由左往右一層一層加入levels

所以採用bfs

因為最後是要從底層往上排列

所以把levels顛倒過來回傳(但還是由左往右)
'''