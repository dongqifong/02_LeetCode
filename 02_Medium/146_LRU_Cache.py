'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
'''

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap={}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            node = Node(key,value)
            if len(self.hashmap)>=self.capacity:
                self.remove(self.tail.prev)
            self.add(node)

        
    def remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.hashmap.pop(node.key)
        return None
    
    def add(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.hashmap[node.key] = node
        return None

'''
本題主要是要訓練
在有限的記憶空間下，如果空間被用盡，那麼要把使用頻率最低的踢出，放入新的資料
而如果呼叫舊資料的話，要更新該資料的使用頻率

所以主要分成兩個部分
第一個部分是hash map，用來記錄key對應到的node
第二個部分是雙向鏈結串列
假設某個時刻狀態是n1-n2-n3
當我呼叫(get)時，n3是最新被調用的，所以順序要改成n3-n1-n2，如果要調用的key(node)沒有在cache裡，回傳-1
當我要放入(put)某個key時，要看當下的key是否有在串列中，但是串列的查詢速度是O(n)，所以用hash map來查，就變成O(1)
如果hash map有這個key，就更新此節點，並且把它掉到串列的頭

不論是get還是put，更新順序都先把舊的節點刪掉(remove)，再把node加入(add)串列的頭，
至於會甚麼要有dummy node(head, tail)，是因為初始狀態是空的，有這個dummy會比較好寫，
也就是有了dummy node，就不用再判斷當前有沒有儲存任何的節點

總結:
結合了hash map跟鏈結串列各自的優點，讓整體的速度是O(1)
hash map查詢速度是快O(1)
鏈結串列搬動資料的方便性O(1)
不論是查詢或搬動資料都沒用到for loop
'''