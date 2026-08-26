import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0)+1

        heap = [(-v, k) for k, v in freq.items()]

        heapq.heapify(heap)

        ans = []

        for i in range(k):
            t = heapq.heappop(heap)
            ans.append(t[1])

        return ans