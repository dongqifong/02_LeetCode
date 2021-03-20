# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        if left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(left-1):
            pre=pre.next
        cur=pre.next
        for i in range(right-left):
            Next=cur.next
            cur.next=Next.next
            Next.next=pre.next
            pre.next=Next
        return dummy.next


'''
方法一：
類似泡沫排序法
兩兩一直對調
範例如下

left=3, right=6

  pre cur Next
1 2   30   40   50   60   7

  pre Next cur
1 2   40   30   50   60   7
  pre      cur  Next
1 2   40   30   50   60   7


  pre Next      cur
1 2   50   40   30   60   7
  pre           cur  Next
1 2   50   40   30   60   7

.
.
.
其中需要先建立一個dummy=ListNode(0)
是為了有可能left=1
確保pre的位置在left前面

方法二：
使用一個額外陣列儲存left-right之間的節點
反轉後再接回去

'''