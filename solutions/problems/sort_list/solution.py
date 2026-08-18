# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeSort(head):
    
            if head is None or head.next is None:
                return head
            
            slow = head
            fast = head
            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            head2 = slow.next
            slow.next = None
            
            L = mergeSort(head)
            R = mergeSort(head2)
            
            dummy = ListNode(0)
            tail = dummy
            
            while L and R:
                if L.val <= R.val:
                    newNode = ListNode(L.val)
                    L = L.next
                    tail.next = newNode
                    tail = tail.next
                else:
                    newNode = ListNode(R.val)
                    R = R.next
                    tail.next = newNode
                    tail = tail.next
            
            while L:
                newNode = ListNode(L.val)
                L = L.next
                tail.next = newNode
                tail = tail.next
                
            while R:
                newNode = ListNode(R.val)
                R = R.next
                tail.next = newNode
                tail = tail.next
                
            return dummy.next
        
        return mergeSort(head)