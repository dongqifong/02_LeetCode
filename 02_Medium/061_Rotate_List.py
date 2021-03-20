# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from os import system
system('cs')
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next is None:
            return head
        q=[]
        dummy=head
        while head:
            q.append(head)
            head=head.next
        L=len(q)
        n=k%L
        if n==0:
            return dummy
        else:
            h=q[-n]
            t=q[-1]
            t.next=q[0]
            q[-n-1].next=None
            return h

'''
1.把串列加到佇列並計算長度->L
2.計算有效循環數n=k%L
3.要循環n次，那h(頭)就會是q[-n]
4.尾部就是q[-1]
5.尾部的next要接到原本的頭q[0]
6.把新的頭部的前一個位置的next改為空-->q[-n-1].next=None
7.return h
'''