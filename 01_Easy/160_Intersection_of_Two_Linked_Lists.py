'''
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pa = headA # 2 pointers
        pb = headB
        while pa!=pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            if pa:
                pa=pa.next
            else:
                pa=headB
            if pb:
                pb=pb.next
            else:
                pb=headA
        return pa