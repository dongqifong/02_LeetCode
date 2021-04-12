'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack=[root]
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if stack:
                cur.right=stack[-1]
            cur.left = None
'''
用額外array的方法有兩種
第一種就是用pre-order方法走訪一次按照順序加入queue
然後按照順序接到root的右邊，然後把左邊改成None

第二種方法適用stack
先把root加入stack
然後把cur指向stack.pop()
第一次就是root
之後看有沒有右節點，有的話加入stack
看左節點有沒有，有的話加入stack

之後如果stack還有值
那代表還沒有全不接到root上
把最後一個node接到cur.right上
但不要pop出去(因為下一個回圈才能pop)
然後把cur.left改成空值

順序就是逐一把左子樹接在cur.right上，所以要先push right進去stack
left才會後進先出

'''