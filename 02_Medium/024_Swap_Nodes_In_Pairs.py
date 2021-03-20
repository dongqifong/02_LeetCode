'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        q=[]
        while head:
            q.append(head)
            head=head.next
        l=len(q)
        if l%2!=0:
            l-=1
        for i in range(0,l,2):
            q[i],q[i+1]=q[i+1],q[i]
        q.append(None)
        dummy=q[0]
        h=q.pop(0)
        while q:
            h.next=q.pop(0)
            h=h.next
        return dummy