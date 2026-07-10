# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        slow = None
        fast = None
        if head:
            slow = head
        if head and head.next:
            fast = head.next

        while fast:
            while fast and slow.val == fast.val:
                fast = fast.next
                
            if not prev and slow.next != fast:
                head = fast
                slow = head
                if fast:
                    fast = fast.next
            elif prev and slow.next != fast:
                prev.next = fast
                slow = fast
                if fast:
                    fast = fast.next
            else:
                prev = slow
                slow = slow.next
                if fast:
                    fast = fast.next

        return head