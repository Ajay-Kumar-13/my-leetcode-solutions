"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        temp = head
        dummy = Node(0)
        tail = dummy
        while temp is not None:
            tail.next = temp
            tail = tail.next

            if temp.child:
                child = self.flatten(temp.child)
                temp2 = tail.next
                tail.next = child
                child.prev = temp
                temp.child = None
                while tail.next:
                    tail = tail.next
                    temp = temp.next
                tail.next = temp2

                if temp2:
                    temp2.prev = tail
                
            temp = temp.next
        
        return dummy.next
