'''
Given the head of a singly linked list, sort the list using insertion sort, 
and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. 
The partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
'''
import os
os.system("clear")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = dummy.next
        
        while cur and cur.next:
            Next_val = cur.next.val
            if cur.val <= Next_val:
                cur = cur.next
                continue
            
            p = dummy
            while p.next.val < Next_val:
                p = p.next
            
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
            
        return dummy.next

'''
有點像泡沫排序法，但是他是linked - list
若cur比cur.next(=Next_val)來得大
代表cur要向後方”浮“
但是Next_val要放在前面的哪個位置就要從p(=dummy)一路向後找，
當p.next>=Next_val時，表示p.next的位置是Next_val之後要放入的位置
接下來就是三個點(p.next,new = cur.next,cur)的對調

以上操作比較到cur.next不存在，代表cur已經在是在linked list的尾部
回傳dummy.next(=head)
'''