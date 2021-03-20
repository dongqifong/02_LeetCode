'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
import os

if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')


class MinStack:

    def __init__(self):
        self.stack=[[0,float('inf')]]
        
    def push(self, x):
        self.stack.append([x,min(x,self.stack[-1][1])])
    def pop(self):
        if len(self.stack)==1:
            return None
        return self.stack.pop()
    def top(self):
        if len(self.stack)==1:
            return None
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]