class Node:
    def __init__ (self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev=None


class LRUCache:

    def remove(self, node): # discards the node needed 
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev 
        
    
    def insert(self,node): #inserts the newly used node
        prev = self.MRUP.prev
        prev.next, node.prev = node, prev
        node.next, self.MRUP.prev = self.MRUP, node
        self.cache[node.key] = node 
        #add to cache 

    def __init__(self, capacity: int):
        self.cache = {} #stores our nodes containng vals for O(1) look ups
        self.cap = capacity #decalres cal to check later 
        self.LRUP = Node()
        self.MRUP = Node() #contains the pointer to the most recently used 
        self.LRUP.next, self.MRUP.prev = self.MRUP, self.LRUP

        

    def get(self, key: int) -> int: # O(1)
        if key in self.cache:
            node = self.cache[key]
            self.remove(self.cache[key])
            self.insert(node) #inserts at MRU 
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None: # O(1)
        
        node = Node(key,value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(node)

        if len(self.cache) > self.cap:
            del self.cache[self.LRUP.next.key] #removes any references to the node
            self.remove(self.LRUP.next)
        
