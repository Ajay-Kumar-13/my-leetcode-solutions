class Solution(object):

    def insert(self, heap, element):
        heap.append(element)
        index = len(heap)-1
        while index > 0 and heap[(index-1)//2][1] < heap[index][1]:
            heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
            index = (index-1)//2

    def pop(self, heap):
        if len(heap) < 2:
            return heap
        
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()

        p = 0
        l = 1
        r = 2 

        while l < len(heap) or r < len(heap):
            if l < len(heap) and r < len(heap):
                if heap[l][1] <= heap[p][1] and heap[r][1] <= heap[p][1]:
                    break
                if heap[l][1] < heap[r][1]:
                    heap[p], heap[r] = heap[r], heap[p]
                    p = r
                else:
                    heap[p], heap[l] = heap[l], heap[p]
                    p = l
            elif l < len(heap):
                if heap[l][1] <= heap[p][1]:
                    break
                if heap[p][1] < heap[l][1]:
                    heap[p], heap[l] = heap[l], heap[p]
                    p = l
            elif r < len(heap):
                if heap[r][1] <= heap[p][1]:
                    break
                if heap[p][1] < heap[r][1]:
                    heap[p], heap[r] = heap[r], heap[p]
                    p = r
            l = p*2+1
            r = p*2+2


    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []

        for i in range(k):
            self.insert(heap, (i, nums[i]))
        
        i = 0
        j = k
        ans = [heap[0][1]]

        while j < len(nums):

            self.insert(heap, (j,nums[j]))
            i += 1
            j += 1

            while heap[0][0] < i:
                self.pop(heap)

            ans.append(heap[0][1])

        return ans