'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        low = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            low = low.next
            if fast == low:
                break
        fast = head
        while fast != low:
            fast = fast.next
            low = low.next
        return low
        
'''
先使用快慢指標，如果有環的話，兩個一定會在環內碰到
如果沒有環的話，那fast.next一定會碰到None
那這時候就直接跳出

接下來，設計兩個指標，一個指向最剛開始的head，另一個放在快慢指標的接觸點
因為這種環狀結構，接觸點會剛好是環的長度
這種情況下，兩個指標每次都往下走一步，最後會在環的起點碰在一起。

補個公式
A+B+nN = 2*(A+B)
A是從head到環開始位置的長度
B是從環的起點位置到快慢指標接觸位置的長度
N代表環的長度
n表示快指標經過了幾次環

這表示慢指標走的長度 = 快指標走的長度- n圈環的長度 = n圈環的長度

'''