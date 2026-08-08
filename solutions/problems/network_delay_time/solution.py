import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distances = {}
        edges = {}

        for i in range(1, n+1):
            distances[i] = float("inf")
            if i == k:
                distances[i] = 0

        for edge in times:
            edges.setdefault(edge[0], []).append((edge[1], edge[2]))
            if edges.get(edge[1], None) is None:
                edges[edge[1]] = []

        heap = []

        heapq.heappush(heap, (0, k))

        visited = set(heap)

        while len(heap) > 0:
            dist, root = heapq.heappop(heap)
            
            for edge in edges.get(root):
                d_u = distances.get(root)
                d_v = distances.get(edge[0])
                c_uv = edge[1]

                if d_u + c_uv < d_v:
                    distances[edge[0]] = d_u + c_uv

                if (distances.get(edge[0]), edge[0]) not in visited:
                    heapq.heappush(heap, (distances.get(edge[0]), edge[0]))
                    visited.add((distances.get(edge[0]), edge[0]))

        minTime = max(distances.values())
        if minTime == float('inf'):
            return -1

        return minTime
            