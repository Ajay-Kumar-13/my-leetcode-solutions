# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)

        dummy.next = head

        head = dummy
        slow = dummy
        fast = dummy.next

        while fast:
            while fast.next and fast.val == val:
                fast = fast.next

            if fast and fast.val == val:
                fast = fast.next

            slow.next = fast
            slow = fast
            if fast:
                fast = fast.next


        return dummy.next