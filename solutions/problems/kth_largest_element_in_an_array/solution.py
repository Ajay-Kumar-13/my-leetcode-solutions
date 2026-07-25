import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
        
        n = len(heap)
        for i in range(n-k):
            heapq.heappop(heap)
        
        return heap[0]
            
        