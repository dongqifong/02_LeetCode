import os

if os.name=='nt':#windows
    os.system('cls')
else:
    os.system('clear')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution():
    def mergeTwoLists(self,l1,l2):
        ptr=ListNode(0)
        ptr_head=ptr
        while l1 and l2:
            if l1.val<=l2.val:
                ptr.next=l1
                l1=l1.next
            else:
                ptr.next=l2
                l2=l2.next
            ptr=ptr.next
        ptr.next=l1 or l2
        return ptr_head.next

def list_node(mylist):
    q=[]
    for i in range(len(mylist)):
        q.append(ListNode(mylist[i]))
    for j in range(len(q)-1):
        q[j].next=q[j+1]
    return q[0]

def print_list(node_head):
    ptr=node_head
    while ptr:
        print(ptr.val)
        ptr=ptr.next

list1=[1,2,4]
q_node=list_node(list1)
print_list(q_node)

    

