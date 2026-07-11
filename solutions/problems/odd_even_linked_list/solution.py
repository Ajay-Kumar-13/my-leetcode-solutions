# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        temp = head
        evenNode = ListNode(0)
        temp2 = evenNode
        while temp:
            if temp and temp.next:
                temp2.next = temp.next
                temp2 = temp2.next
                
                
                # Link odd nodes
                temp.next = temp.next.next
                if temp.next:
                    temp = temp.next
                
                temp2.next = None
            else:
                break

        temp.next = evenNode.next

        return head