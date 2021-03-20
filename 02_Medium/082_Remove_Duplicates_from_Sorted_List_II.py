'''
Given the head of a sorted linked list, 
delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start=ListNode(0)
        dummy=start
        count=1
        while head and head.next:
            if head.val==head.next.val:
                count+=1
            else:
                if count==1:
                    start.next=head
                    start=start.next
                else:
                    count=1
            head=head.next
        if count==1:
            start.next=head
            start=start.next
        else:
            start.next=None
        return dummy.next
'''
以start起頭
count計算遇過的次數
一直比較head和head.next
若不相同且count==1
才能把head節點加到start.next
最後跳出while的時候
head就是在最後一個節點
若count==1表示需要再接到start.next
否則start.next要設為None
最後return dummy.next
(因為dummy起始值是節點0)
'''