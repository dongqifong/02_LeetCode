'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        curr = head
        list_size = self.list_size(curr)
        batch_size = 1
        dummy = ListNode(val = 0, next = head)
        while batch_size < list_size:
            tail = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = self.split(left, batch_size) # left後方一個batchsize跟後面斷開
                curr = self.split(right, batch_size) # right後方一個batchsize跟後面斷開
                tail = self.merge(tail, left, right) # 合併left,right list
            batch_size *= 2 # 因為倆倆合併，所以batch_size以2^n速度成長
        return dummy.next
    
    def merge(self, tail: ListNode, l1: ListNode, l2: ListNode):       
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1 or l2:
            tail.next = l1 or l2
            while tail and tail.next:
                tail = tail.next
        return tail

    def split(self, node: ListNode, batch_size: int) -> ListNode:
        if not node:
            return node
        prev = None
        curr = node
        while batch_size > 0 and curr:
            prev = curr
            curr = curr.next
            batch_size -= 1     
        prev.next = None
        return curr
    
    def list_size(self, node: ListNode):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

'''
在最糟的情況下時間複雜度是O(nlogn)及固定space才符合題意
所以想到的方法是用分治法的merge sort
但是一般的分治法，是top down，採用遞迴方法，沒辦法做到固定space = O(1)
改成用bottom up及while迴圈的方法才可以辦到space = O(1)

想法是將一個list切成小小的片段，最小是1
切的過程要將list斷開
之後兩兩merge list
每merge一輪後(某batch size下，整個list都被split及merge)
因為是兩兩merge，所以下次的batch size就會成長2倍，

'''