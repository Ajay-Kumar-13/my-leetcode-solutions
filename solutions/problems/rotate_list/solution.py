class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        if not head:
            return head

        fast = head

        length = 1
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            length += 2

        if fast.next:
            length += 1

        pushNodesBy = k % length
        
        if pushNodesBy <= 0:
            return head

        temp = head
        for i in range(length-pushNodesBy-1):
            temp = temp.next

        nextChain = temp.next
        temp.next = None

        if nextChain:
            temp = head
            head = nextChain
            tail = head

            while tail.next:
                tail = tail.next

            tail.next = temp

        return head