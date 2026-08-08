from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        m = len(grid)
        n = len(grid[0])

        totalIslands = 0

        visited = set([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    totalIslands += 1
                    q = deque([(i, j)])
                    while len(q) > 0:
                        d, r = q.popleft()

                        if r < n-1 and grid[d][r+1] == "1":
                            q.append((d, r+1))
                            visited.add((d, r+1))
                            grid[d][r+1] = "0"
                        
                        if d < m-1 and grid[d+1][r] == "1":
                            q.append((d+1, r))
                            visited.add((d+1, r))
                            grid[d+1][r] = "0"

                        if r > 0 and grid[d][r-1] == "1":
                            q.append((d, r-1))
                            visited.add((d, r-1))
                            grid[d][r-1] = "0"

                        if d > 0 and grid[d-1][r] == "1":
                            q.append((d-1, r))
                            visited.add((d-1, r))
                            grid[d-1][r] = "0"
        return totalIslands