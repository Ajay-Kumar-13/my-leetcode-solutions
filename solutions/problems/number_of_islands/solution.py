from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    q = deque([[i,j]])
                    grid[i][j] = '0'

                    while len(q) > 0:
                        u, d = q.popleft()
                        
                        if u < m-1 and grid[u+1][d] == "1":
                            q.append([u+1,d])
                            grid[u+1][d] = '0'
                        if d < n-1 and grid[u][d+1] == "1":
                            q.append([u,d+1])
                            grid[u][d+1] = '0'
                        if u > 0 and grid[u-1][d] == "1":     
                            q.append([u-1,d])
                            grid[u-1][d] = '0'
                        if d > 0 and grid[u][d-1] == "1":
                            q.append([u,d-1])
                            grid[u][d-1] = '0'

        return count