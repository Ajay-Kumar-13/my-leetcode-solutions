# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        # find mid
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        head2 = slow.next
        slow.next = None
        slow = None

        # reverse second half
        temp = head2
        before = None
        while temp:
            nextNode = temp.next
            temp.next = before
            before = temp
            temp = nextNode
        head2 = before
            
        # clear pointers
        fast = None
        before = None


        temp1 = head
        temp2 = head2

        while temp1 and temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next

        return True