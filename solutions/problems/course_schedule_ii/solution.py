from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        incomingEdges = {}
        edges = {}
        noIncomingEdges = {}

        for i in range(numCourses):
            noIncomingEdges[i] = i
            
        for e in prerequisites:
            edges.setdefault(e[1], []).append(e[0])
            incomingEdges.setdefault(e[0], []).append(e[1])

            if noIncomingEdges.get(e[0]) is not None:
                del noIncomingEdges[e[0]]

        q = deque(list(noIncomingEdges.values()))
        result = []

        while len(q) > 0:
            course = q.popleft()
            result.append(course)
            for edge in edges.get(course, []):
                if incomingEdges.get(edge, []):
                    incomingEdges.get(edge).pop()
                
                if not incomingEdges.get(edge):
                    q.append(edge)

        if len(result) == numCourses:
            return result
        
        return []