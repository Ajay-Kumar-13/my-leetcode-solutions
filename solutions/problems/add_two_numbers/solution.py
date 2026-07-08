# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp1 = l1
        temp2 = l2

        num1 = []
        num2 = []

        while temp1 or temp2:
            if temp1:
                num1.append(str(temp1.val))
                temp1 = temp1.next

            if temp2:
                num2.append(str(temp2.val))
                temp2 = temp2.next
        
        num1.reverse()
        num2.reverse()
        num1 = int("".join(num1))
        num2 = int("".join(num2))

        ans = list(str(num1+num2))

        ans.reverse()

        s = ListNode()
        temp = s
        for n in ans:
            newNode = ListNode(int(n))
            temp.next = newNode
            temp = temp.next

        return s.next