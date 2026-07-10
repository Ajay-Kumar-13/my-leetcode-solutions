# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []

        sorted_list = ListNode()

        def insert(heap, element):
            
            heap.append(element)
            index = len(heap)-1
            
            while index > 0 and heap[index] < heap[(index-1) // 2]:
                heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
                index = (index-1) // 2
                
        def pop():
            
            if not min_heap:
                return
            
            if len(min_heap) < 2:
                return min_heap.pop()
            
            min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
            element = min_heap.pop()
            
            root = 0
            
            while True:
                left_child = (2*root)+1
                right_child = (2*root)+2
                
                # Node has both children
                if left_child < len(min_heap) and right_child < len(min_heap):
                    # current node is smaller or equal to its children
                    if min_heap[root] <= min(min_heap[left_child], min_heap[right_child]):
                        break
                    if min_heap[right_child] > min_heap[left_child]:
                        min_heap[root], min_heap[left_child] = min_heap[left_child], min_heap[root]
                        root = left_child
                    else:
                        min_heap[root], min_heap[right_child] = min_heap[right_child], min_heap[root]
                        root = right_child
                # Node has only left child
                elif left_child < len(min_heap):
                    if min_heap[root] > min_heap[left_child]:
                        min_heap[root], min_heap[left_child] = min_heap[left_child], min_heap[root]
                        root = left_child
                    else:    
                        break
                # Node has only right child
                elif right_child < len(min_heap):
                    if min_heap[root] > min_heap[right_child]:
                        min_heap[root], min_heap[right_child] = min_heap[right_child], min_heap[root]
                        root = right_child
                    else:    
                        break
                # Leaf Node
                else:
                    break
                
            return element

        for l in lists:
            temp = l
            while temp is not None:
                insert(min_heap, temp.val)
                temp = temp.next

        temp = sorted_list
        for i in range(len(min_heap)):
            newNode = ListNode(pop())
            temp.next = newNode
            temp = temp.next
            
        return sorted_list.next       