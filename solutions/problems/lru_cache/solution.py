class Node:
    def __init__(self,key=0, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.key = key
        self.next = next
    
    def insertBeforeHead(self, key, value, head):
        existingChain = head.next
        newNode = Node(key, value)
        head.next = newNode
        newNode.prev = head
        
        newNode.next = existingChain
        if existingChain:
            existingChain.prev = newNode
        
        return newNode
        
    def makeHead(self, node, head):
        
        # If node is head
        if node.prev == head:
            return
        
        existingChain = head.next
        
        # will take care of before and after nodes
        node.next.prev = node.prev
        node.prev.next = node.next
        
        # Since the current node is a head
        node.prev = head
        
        # making it a head
        head.next = node
        
        # link the chain to the new head
        node.next = existingChain
        existingChain.prev = node
                
    def removeTail(self, node):
        if not node:
            return 
        if node.prev:
            node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = None
        node.prev = None
        
        return node
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.memory = Node(0,0)
        self.tail = Node(0,0)
        
        self.memory.next = self.tail
        self.tail.prev = self.memory

    def get(self, key):
        
        target_node = self.cache.get(key, -1)
        if target_node != -1:
            self.memory.makeHead(target_node, self.memory)
            return target_node.val
        else:
            return -1

    def put(self, key, value):
        existingNode = self.cache.get(key, None)
        if existingNode:
            existingNode.val = value
            self.memory.makeHead(existingNode, self.memory)
        else:
            if len(self.cache) >= self.capacity:
                LRU = self.memory.removeTail(self.tail.prev)
                if LRU:
                    del self.cache[LRU.key]
            node = self.memory.insertBeforeHead(key, value, self.memory)
            self.cache[key] = node