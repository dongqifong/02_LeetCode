'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue=[]
        queue.append(node)
        visited={}
        visited[node]=Node(node.val,[])
        
        while queue:
            n=queue.pop(0) # old graph's node
            for neighbor in n.neighbors:
                if neighbor not in visited: # new graph's node
                    visited[neighbor]=Node(neighbor.val,[])
                    queue.append(neighbor) # old graph's node
                visited[n].neighbors.append(visited[neighbor]) # connect to new graph's neighbor
        return visited[node]
        

'''
以queue作為bfs的容器，visited紀錄clone的新節點

每經過“舊”圖(graph)的node，就看看他的neighbors存不存在visited字典裡面
若沒有的話就把它加到visited內，並加入queue
之後連接visited[n]節點到新的neighbor，
循環到queue為空
就代表“舊”圖所有節點都走完了，而且也clone一個新的graph
'''