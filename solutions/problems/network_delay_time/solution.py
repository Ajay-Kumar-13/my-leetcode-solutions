import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        outgoingEdges = {}
        distances = {}

        for i in range(1, n+1):
            outgoingEdges[i] = []
            distances[i] = float('inf')

        distances[k] = 0

        for edge in times:
            outgoingEdges.setdefault(edge[0], []).append([edge[0], edge[1], edge[2]])

        visited = set()

        heap = [(0, k)]

        while heap:
            current = heapq.heappop(heap)

            if current[1] in visited:
                continue

            visited.add(current[1])

            for edge in outgoingEdges.get(current[1]):
                
                if distances.get(edge[0]) + edge[2] < distances.get(edge[1]):
                    distances[edge[1]] = distances.get(edge[0]) + edge[2]
                
                heapq.heappush(heap, (distances.get(edge[1]), edge[1]))


        if len(visited) != n:
            return -1
        
        return max(list(distances.values()))