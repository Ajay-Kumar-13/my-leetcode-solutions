class Solution:
    def removeNthFromEnd(self, head, n):
        
        temp = head

        slow = temp
        fast = temp

        for i in range(n):
            fast = fast.next

        if not fast:
            return slow.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head