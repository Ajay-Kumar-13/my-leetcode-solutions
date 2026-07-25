class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity

        self.dummyHead = Node(-1, -1)
        self.dummyTail = Node(-1, -1)

        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def adjustChain(self, node):

        # link prev node of the current node to the next node
        node.prev.next = node.next
        node.next.prev = node.prev

        head = self.dummyHead.next

        # Link the new node to the dummy as head
        self.dummyHead.next = node
        node.prev = self.dummyHead

        # link the existing chain to the new head
        node.next = head
        head.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)

        if node is not None:
            self.adjustChain(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Removes the least used node in the linked list
        def removeLeastUsedNode():
            del self.cache[self.dummyTail.prev.key]

            tail = self.dummyTail.prev.prev

            # update the tail, delete the last node(original tail)
            tail.next = self.dummyTail
            self.dummyTail.prev = tail

        node = self.cache.get(key, None)

        if node is not None:
            node.val = value

            # link prev node of the current node to the next node
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
            if len(self.cache) >= self.capacity:
                removeLeastUsedNode()
            self.cache[key] = node

        head = self.dummyHead.next

        # Link the new node to the dummy as head
        self.dummyHead.next = node
        node.prev = self.dummyHead

        # link the existing chain to the new head
        node.next = head
        head.prev = node
