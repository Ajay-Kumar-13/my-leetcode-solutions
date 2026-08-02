# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        prev = head
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Break the list
        prev.next = None

        head1 = head
        head2 = slow

        # reverse the second list

        temp = head2
        prev = None
        next = temp.next
        while next:
            temp.next = prev
            prev = temp
            temp = next
            next = next.next
        
        temp.next = prev
        head2 = temp

        # re-order the list

        next1 = head1
        next2 = head2

        i = 0
        while next1 and next2 and next1 != next2:
 
            if i % 2 != 0:
                prev = next2
                next2 = next2.next
                next = next1
                prev.next = next
            else:
                prev = next1
                next1 = next1.next
                next = next2
                prev.next = next
            i += 1