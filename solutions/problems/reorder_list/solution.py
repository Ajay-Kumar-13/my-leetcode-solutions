# Definition for singly-linked list.
# cl    ass ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Find the middle of linked list
        temp = head
        slow = temp
        fast = temp.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # Reverse the second half
        temp = head2
        beforeNode = None
        prev = None
        while temp is not None:
            prev = temp
            temp = temp.next
            prev.next = beforeNode
            beforeNode = prev


        # merge the two lists
        first = head
        second = prev
        while second:
            
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2