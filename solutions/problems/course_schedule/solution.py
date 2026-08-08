from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        outgoing = {}
        incoming = {}

        for i in range(numCourses):
            incoming[i] = 0

        for edge in prerequisites:
            outgoing.setdefault(edge[1], []).append(edge[0])
            
            incoming[edge[0]] = incoming.get(edge[0], 0)+1
            if incoming.get(edge[1], None) is None:
                incoming[edge[1]] = 0


        q = deque([])
        finishedCourses = 0

        for k,v in incoming.items():
            if v == 0:
                q.append(k)

        while len(q) > 0:
            edge = q.popleft()
            finishedCourses += 1
            outgoingEdges = outgoing.get(edge, [])

            while len(outgoingEdges) > 0:
                edge = outgoingEdges.pop()

                count = incoming.get(edge, 0)
                if count > 0:
                    incoming[edge] = incoming.get(edge) - 1
                    if incoming.get(edge) == 0:
                        q.append(edge)

        print(finishedCourses)
        if finishedCourses == numCourses:
            return True

        return False