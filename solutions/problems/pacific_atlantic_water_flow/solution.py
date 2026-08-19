from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:   

        m = len(heights)
        n = len(heights[0])

        pacific_border = []
        atlantic_border = []

        for i in range(n):
            pacific_border.append((0, i))

        for i in range(1, m):
            pacific_border.append((i, 0))

        for i in range(n-1):
            atlantic_border.append((m-1, i))
        
        for i in range(m):
            atlantic_border.append((i, n-1))

        def findSol(que):
            q = deque(que)
            visited = set(que)

            while len(q) > 0:
                i, j = q.popleft()

                if j < n-1 and heights[i][j] <= heights[i][j+1] and (i, j+1) not in visited:
                    q.append((i, j+1))
                    visited.add((i, j+1))
                if j > 0 and heights[i][j] <= heights[i][j-1] and (i, j-1) not in visited:
                    q.append((i, j-1))
                    visited.add((i, j-1))
                if i > 0 and heights[i][j] <= heights[i-1][j] and (i-1, j) not in visited:
                    q.append((i-1, j))
                    visited.add((i-1, j))
                if i < m-1 and heights[i][j] <= heights[i+1][j] and (i+1, j) not in visited:
                    q.append((i+1, j))
                    visited.add((i+1, j))

            return visited

        return list(findSol(pacific_border).intersection(findSol(atlantic_border)))