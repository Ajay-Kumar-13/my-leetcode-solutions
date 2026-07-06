# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = head
        before = None
        while temp is not None:
            prev = temp
            temp = temp.next
            prev.next = before
            before = prev

        head = before

        return head