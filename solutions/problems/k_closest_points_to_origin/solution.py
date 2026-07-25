import heapq
import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        
        
        def calculateDistance(x, y):
            num = (x*x) + (y*y)
            return math.sqrt(num)

        heap = []
        for point in points:
            heapq.heappush(heap, (calculateDistance(point[0], point[1]), point))

        result = []
        for i in range(k):
            point = heap[0][1]
            result.append(point)
            heapq.heappop(heap)

        return result