'''
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s=ListNode(0)
        l=ListNode(0)
        dummy_s=s
        dummy_l=l
        while head:
            if head.val<x:
                s.next=head
                s=s.next
            else:
                l.next=head
                l=l.next
            head=head.next
        
        l.next=None
        s.next=dummy_l.next
        return dummy_s.next

'''
分兩支來看
s負責找比x小的節點串起來
l負責找大於或等於x的節點串起來
接完以後l.next要設為空值
不然會有circle
最後把dummy_l.next接到s.next上
回傳dummy_s.next
'''