# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def mergeSort(head):
    
            if not head or head.next is None:
                return head
                
            mid = head
            fast = head.next
            
            while fast and fast.next:
                mid = mid.next
                fast = fast.next.next
                
            
            r_chain = mid.next
            mid.next = None
            
            left = mergeSort(head)
            right = mergeSort(r_chain)

            dummy = ListNode(0)
            tail = dummy
            
            while left and right:
                if left.val >= right.val and left != right:
                    temp = right.next
                    tail.next = right
                    tail = tail.next
                    tail.next = None
                    right = temp
                else:
                    temp = left.next
                    tail.next = left
                    tail = tail.next
                    tail.next = None
                    left = temp
                    
            while left:
                tail.next = left
                tail = tail.next
                left = left.next
                
            while right:
                tail.next = right
                tail = tail.next
                right = right.next
                    
            return dummy.next

        head = mergeSort(head)
        return head