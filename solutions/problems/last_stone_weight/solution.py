import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            x = -(heapq.heappop(max_heap))
            y = -(heapq.heappop(max_heap))

            if (x-y) != 0:
                heapq.heappush(max_heap, -(x-y))

        if len(max_heap) > 0:
            return -max_heap[0]

        return 0