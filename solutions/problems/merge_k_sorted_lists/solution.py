# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        head = None
        tail = None
        i = len(lists)
        while len(heap) > 0:
            val, counter, node = heapq.heappop(heap)
            if head is None:
                head = ListNode(node.val)
                tail = head
            else:
                tail.next = ListNode(node.val)
                tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1

        return head
