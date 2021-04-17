'''
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q=[root,None]
        while q:
            if q[0]==None:
                return root
            for i in range(len(q)-1):
                q[0].next=q[1]
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.pop(0)
            q.pop(0)# pop None at head
            q.append(None)# append None at tail

'''
第一種方法，可以同一個code同時解非完滿二元樹(Perfect Binary Tree)
用BFS一層一層往下走
但最末端要多加一個None
才能同時辦到將左節點和右節點append到下階段的佇列
及將next連到下個右邊節點

第二種方法是用level i對level i+1進行操作
假設level i=[2,3]
那就是把level i 每個節點的左節點連到右節點，右節點連接到level i下個節點的左節點
e.g.
node(it's left or right node)
2(4)->2(5)
2(5)->3(6)
3(6)->3(7)

當走到最右邊會碰到，3.next是None
所以3(7)的next就不用操作
if not level[i].left:
    return root

if level[i].next!=None:
    level[i].left.next=level[i].right
    level[i].right.next=level[i+1].left
else:
    level[i].left.next=level[i].right
但第二種若碰到非perfect Binery Tree就要額外判斷
右邊的節點存不存在
沒辦法直接用level[i].left.next=level[i].right

'''