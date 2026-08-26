import heapq

class Solution:
    def leastInterval(self, tasks, n):
        
        taskFreq = {}
        
        for t in tasks:
            taskFreq[t] = taskFreq.get(t, 0) + 1 

        heap =[(-v,k) for k,v in taskFreq.items()]

        heapq.heapify(heap)
        
        intervals = 0

        while len(heap) > 0:

            iterations = 0

            tuples = []

            while len(heap) > 0 and iterations < n+1:
                t = heapq.heappop(heap)

                freq = -t[0]
                if freq-1 > 0:
                    tuples.append((-(freq-1), t[1]))

                iterations += 1
                intervals += 1

            if len(tuples) > 0 and iterations < n+1:
                intervals += ((n+1)-iterations)

            for t in tuples:
                heapq.heappush(heap, t)
            

        return intervals