from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        max_area = 0    
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 1
                    q = deque([[i, j]])
                    grid[i][j] = 0

                    while len(q) > 0:
                        u, d = q.popleft()

                        if u < m-1 and grid[u+1][d] == 1:
                            q.append([u+1,d])
                            grid[u+1][d] = 0
                            area += 1
                        if u > 0 and grid[u-1][d] == 1:
                            q.append([u-1,d])
                            grid[u-1][d] = 0
                            area += 1
                        if d < n-1 and grid[u][d+1] == 1:
                            q.append([u,d+1])
                            grid[u][d+1] = 0
                            area += 1
                        if d > 0 and grid[u][d-1] == 1:
                            q.append([u,d-1])
                            grid[u][d-1] = 0
                            area += 1
                    
                    max_area = max(area, max_area)

        return max_area
