"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = {}

        if not head:
            return None
    
        newHead = None
        
        temp1 = head
        temp2 = newHead

        while temp1:
            
            node = nodes.get(temp1, None)
            if node is None:
                node = Node(temp1.val)
                nodes[temp1] = node

            if newHead is None:
                newHead = node
                temp2 = newHead
            else:
                temp2.next = node
                temp2 = temp2.next

            randomNode = nodes.get(temp1.random, None)
            if randomNode is None and temp1.random is not None:
                randomNode = Node(temp1.random.val)
                nodes[temp1.random] = randomNode
            
            temp2.random = randomNode

            temp1 = temp1.next

        return newHead