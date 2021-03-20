'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        q=[]
        dummy=head
        while head:
            q.append(head)
            head=head.next
        if n==1:
            q[len(q)-1-n].next=None
            return dummy
        if n==len(q):
            return q[1]
        q[len(q)-1-n].next=q[len(q)-n+1]
        return dummy