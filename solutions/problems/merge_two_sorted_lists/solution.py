# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp1 = list1
        temp2 = list2
        sl = None

        SortedList = None

        while True:
            if temp1 is not None and temp2 is not None and temp1.val <= temp2.val:
                node = ListNode(temp1.val)
                if SortedList is None:
                    SortedList = node
                    sl = SortedList
                else:
                    sl.next = node
                    sl = sl.next
                temp1 = temp1.next
            elif temp2 is not None and temp1 is not None and temp2.val < temp1.val:
                node = ListNode(temp2.val)
                if SortedList is None:
                    SortedList = node
                    sl = SortedList
                else:
                    sl.next = node
                    sl = sl.next
                temp2 = temp2.next
            else:
                break

        while temp1 is not None:
            node = ListNode(temp1.val)
            if SortedList is None:
                SortedList = node
                sl = SortedList
            else:
                sl.next = node
                sl = sl.next
            temp1 = temp1.next

        while temp2 is not None:
            node = ListNode(temp2.val)
            if SortedList is None:
                SortedList = node
                sl = SortedList
            else:
                sl.next = node
                sl = sl.next
            temp2 = temp2.next

        return SortedList