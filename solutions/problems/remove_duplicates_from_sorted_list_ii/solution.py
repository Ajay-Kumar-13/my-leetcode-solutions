class Solution:
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        dummy.next = head
        
        temp = head
        prev = dummy
        
        while temp:
        
            while temp and temp.next and temp.val == temp.next.val:
                temp = temp.next
            
            if prev.next != temp:
                prev.next = temp.next
            else:
                prev = temp
            
            temp = temp.next

        return dummy.next
        