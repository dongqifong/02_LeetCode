'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # 找中點
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
                    
        # 反轉link list 後半部
        pre = None
        cur = slow.next
        slow.next = None
        while cur:
            nextt = cur.next
            cur.next=pre
            pre = cur
            cur = nextt
        
        # 前半段和後半段合併
        head1 = head
        head2 = pre
        while head2:
            nextt = head1.next
            head1.next=head2
            head1 = head2
            head2 = nextt
        return None

'''
方法一：

第一：找中點
這點其實是觀察出來的，因為左半部每個節點，都要配右半部一個節點

第二：反轉後半部linked list
因為配對方法是第一個配最後一個，第二個配倒數第二個，依此類推
因此先將後半部反轉過來

第三：把前半部和後半部合併起來

優點：不用額外配置記憶體，速度快
缺點：比較不直觀，要先熟練快慢指標、反轉linked list

方法二：

直接把每個節點都append到一個陣列裡
然後重新連結

優點：很直觀
缺點：但是要額外空間，速度也不如方法一
'''