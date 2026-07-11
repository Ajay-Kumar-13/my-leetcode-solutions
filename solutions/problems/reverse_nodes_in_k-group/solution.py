# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        dummy = None

        slow = head
        fast = head

        n = 0

        while True:
            existingChain = slow
            nextChain = None
            
            while fast:
                fast = fast.next
                if fast:
                    n += 1
                    if n == k and fast:
                        nextChain = fast.next
                        fast.next = None
                        fast = None
                        break
                
            if n < k:
                break
            
            slow = slow.next
            existingChain.next = None
            
            before = None
            tail = slow
            while slow:
                nextNode = slow.next
                slow.next = before
                before = slow
                slow = nextNode
                
            existingChain.next = before
            before = None
            tail.next = nextChain
            slow = tail
            fast = tail
            tail = None
            
            n = 0

        return head.next