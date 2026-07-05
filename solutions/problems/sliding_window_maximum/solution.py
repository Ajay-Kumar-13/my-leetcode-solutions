class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Insert into the heap
        def insert(heap, index):
            heap.append((nums[index], index))
            index = len(heap) - 1
            while index > 0 and heap[(index-1)//2][0] < heap[index][0]:
                heap[(index-1) // 2], heap[index] = heap[index], heap[(index-1) // 2]
                index = (index - 1) // 2    
        # Delete the element and heapify the entire heap. 
        def pop(heap):
            # swap this element in ith index with the last index
            heap[-1], heap[0] = heap[0], heap[-1]
            # now pop the last element
            heap.pop()
            i = 0
            while True:
                # find children of that node
                left_child = 2*i+1
                right_child = 2*i+2
                # If node has two childrens, swap with the max node
                if len(heap) > left_child and len(heap) > right_child:
                    if heap[left_child][0] <= heap[i][0] and heap[right_child][0] <= heap[i][0]:
                        break
                    if heap[left_child][0] > heap[right_child][0]:
                        heap[i], heap[left_child] = heap[left_child], heap[i]
                        i = left_child
                    else:
                        heap[i], heap[right_child] = heap[right_child], heap[i]
                        i = right_child
                # If node has only one left child
                elif len(heap) > left_child:
                    if heap[left_child][0] >= heap[i][0]:
                        heap[i], heap[left_child] = heap[left_child], heap[i]
                        i = left_child
                    else:
                        break
                # If node has only one right child
                elif len(heap) > right_child:
                    if heap[right_child][0] >= heap[i][0]:
                        heap[i], heap[right_child] = heap[right_child], heap[i]
                        i = right_child   
                    else:
                        break
                # If node is a left node
                else:
                    break
        # heap array
        heap = []
        # For storing the max elements in the each window
        ans = []
        for i in range(k):
            insert(heap, i)
        ans.append(heap[0][0])

        i = 0
        j = k
        while j < len(nums):
            insert(heap, j)
            j += 1
            i += 1

            while heap[0][1] < i:
                pop(heap)
            
            ans.append(heap[0][0])
        return ans