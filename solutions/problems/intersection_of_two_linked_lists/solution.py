# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        temp1 = headA
        temp2 = headB

        secondPassForHeadA = True
        secondPassForHeadB = True

        while temp1 and temp2:

            if temp1 == temp2:
                return temp1

            if temp1:
                temp1 = temp1.next
            
            if temp1 is None and secondPassForHeadA:
                secondPassForHeadA = False
                temp1 = headB

            if temp2:
                temp2 = temp2.next
                
            if temp2 is None and secondPassForHeadB:
                secondPassForHeadB = False
                temp2 = headA

        return None