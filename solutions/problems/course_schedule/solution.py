from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # BFS
        incomingNodes = {}  
        edgesOfNodes = {}
        noIncomingNodes = {}

        for i in range(numCourses):
            noIncomingNodes[i] = i
        
        for e in prerequisites:
            incomingNodes.setdefault(e[0], []).append(e[1])
            edgesOfNodes.setdefault(e[1], []).append(e[0])
            if noIncomingNodes.get(e[0], None) is not None:
                del noIncomingNodes[e[0]]

        zeroIncomingEdges = deque(list(noIncomingNodes.values()))

        visited = set(zeroIncomingEdges)

        totalUnlockedCourses = 0

        while len(zeroIncomingEdges) > 0:
            course = zeroIncomingEdges.popleft()
            totalUnlockedCourses += 1
            edge = edgesOfNodes.get(course, [])
        
            for e in edge:
                incomingNodes.get(e).pop()
                if not incomingNodes.get(e) and e not in visited:
                    zeroIncomingEdges.append(e)
                    visited.add(e)
            
        return totalUnlockedCourses == numCourses