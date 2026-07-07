"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        random_nodes = {}
        
        dummy = Node(0)

        temp1 = head
        temp2 = dummy

        while temp1 is not None:
            
            newNode = Node(temp1.val)

            previousNode = random_nodes.get(temp1, None) 
            randomNode = None
            if temp1.random:
                randomNode = random_nodes.get(temp1.random, None)

            if previousNode is not None:
                newNode = previousNode
            
            temp2.next = newNode

            random_nodes[temp1] = newNode

            if temp1.random is None:
                temp2.next.random = None
            elif randomNode:
                temp2.next.random = randomNode
            else:
                newNode = Node(temp1.random.val)
                if temp1.random:
                    randomNode = random_nodes.get(temp1.random, None)
                    if randomNode:
                        newNode = randomNode
                random_nodes[temp1.random] = newNode
                temp2.next.random = newNode

            temp1 = temp1.next
            temp2 = temp2.next

        return dummy.next