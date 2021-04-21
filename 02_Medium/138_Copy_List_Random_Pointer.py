"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        q=[]
        q.append(head)
        visited={}
        visited[head]=Node(head.val)
        
        while q:
            n=q.pop(0)
            if n.next:
                q.append(n.next)
                if n.next not in visited:
                    visited[n.next]=Node(n.next.val)
                visited[n].next=visited[n.next]
            if n.random:
                if n.random not in visited:
                    visited[n.random]=Node(n.random.val)
                visited[n].random=visited[n.random]
        return visited[head]
        
'''
本題和clone_Graph相似，使用BFS
每經過一個節點，若此節點有next，就把此next加入q內
接著判斷此next是否有看過，若是沒看過就把它變成一個新的Node加入visited內
之後新節點的next要接新的next節點(在visited內)

next判斷完，看他有沒有random，若有的話就看random的節點是否有看過
沒看過就變成新的節點加入visited
然後新節點.random要連到新的radom

'''