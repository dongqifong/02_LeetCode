import os
os.system('clear')

class node():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def insert(self,mylist)->list:        
        mylist_len=len(mylist)
        q=[]
        for i in mylist:
            q.append(node(i))
        if ((mylist_len-1)-2)%2!=0:
            i_limit=((mylist_len-1)-1)//2
        else:
            i_limit=((mylist_len-1)-2)//2
        for i in range(i_limit+1):#range from 0 ~ i_limit
            if 2*i+1<mylist_len:
                q[i].left=q[2*i+1]
            if 2*i+2<mylist_len:
                q[i].right=q[2*i+2]
        return q

class Solution():
    def levelOrderBottom(self, root)->list:
        from collections import deque
        if root is None:
            return []
        q=deque()
        levels=[]
        level=0
        q.append(root)
        while q:
            level_len=len(q)
            levels.append([])
            for i in range(level_len):
                node=q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return levels




mylist=[0,1,2,None,None,5,6]
node_obj=node()
q=node_obj.insert(mylist)

s=Solution()
result=s.levelOrderBottom(q[0])
print(result)
print(q[1].left.val)
print(q[1].right.val)