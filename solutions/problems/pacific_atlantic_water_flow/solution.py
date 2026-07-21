from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
                
        m = len(heights)
        n = len(heights[0])

        pacific = deque([])
        atlantic = deque([])

        for i in range(n):
            pacific.append((0, i))

        for i in range(1,m):
            pacific.append((i, 0))

        for i in range(n):
            atlantic.append((m-1, i))

        for i in range(m-1):
            atlantic.append((i, n-1))

        def findPath(q):
            
            visited = set()
            found_way_to_pacific = False
            found_way_to_atlanctic = False

            while len(q) > 0:
                
                x, y = q.popleft()

                visited.add((x,y))
                
                current_height = heights[x][y]

                if x > 0 and current_height <= heights[x-1][y] and (x-1, y) not in visited:
                    q.append((x-1, y))
                    visited.add((x-1, y))
                if x < m-1 and current_height <= heights[x+1][y] and (x+1, y) not in visited:
                    q.append((x+1, y))
                    visited.add((x+1, y))
                if y < n-1 and current_height <= heights[x][y+1] and (x, y+1) not in visited:
                    q.append((x, y+1))
                    visited.add((x, y+1))
                if y > 0 and current_height <= heights[x][y-1] and (x, y-1) not in visited:
                    q.append((x, y-1))
                    visited.add((x, y-1))
            
            return visited

        return list(findPath(pacific).intersection(findPath(atlantic)))