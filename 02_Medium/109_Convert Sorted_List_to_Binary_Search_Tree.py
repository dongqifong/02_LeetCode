'''
Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if not head:
            return None
        
        if head.next==None:
            return TreeNode(head.val)
        
        def findmid(head):
            slow=head
            fast=head
            pre=None
            while fast and fast.next:
                pre=slow
                slow=slow.next
                fast=fast.next.next
            pre.next=None
            return slow
        mid=findmid(head)
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
        
'''
要建立一個平衡(height-balanced)的BST就要同時滿足兩個條件
BST: 任意根節點的左子樹數直接小於根節點，右子樹大於根節點
平衡: 任意節點的左子數和右子數層數差距最大為1

因為給定的link list是排序好的
可以把他想成array
每次把中點抓出來當根節點
中點的左半部就是左子樹
右半部就是右子樹

但因為是link list只能靠走訪來query每個節點，為了要找出中間點
要設計slow和fast指標，fast跑得速度為slow的兩倍，這樣當fast.next為空時
slow就是坐在中點了
但因為slow的前一個節點要和slow斷開
所以要多一個pre他會跟在slow前面，當找到中點的時候，pre.next指定成None

一直遞迴這個過程就會把height-balanced BST給建好了

本題跟easy的108很像，但easy的是給sorted的array
可以直接找中點=len(array)//2

link list就要靠快慢指標去走訪
'''