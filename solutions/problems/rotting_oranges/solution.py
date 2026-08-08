from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque([])

        m = len(grid)
        n = len(grid[0])

        totalOranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    totalOranges += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        rottenOranges = len(q)
        totalMinutes = 0

        visited = set(q)

        while len(q) > 0:
            u,v,t = q.popleft()
            totalMinutes = max(totalMinutes, t)

            if v < n-1 and grid[u][v+1] == 1 and (u, v+1) not in visited:
                q.append((u, v+1, t+1))
                visited.add((u, v+1))
                rottenOranges += 1

            if v > 0 and grid[u][v-1] == 1 and (u, v-1) not in visited:
                q.append((u, v-1, t+1))
                visited.add((u, v-1))
                rottenOranges += 1

            if u < m-1 and grid[u+1][v] == 1 and (u+1, v) not in visited:
                q.append((u+1, v, t+1))
                visited.add((u+1, v))
                rottenOranges += 1

            if u > 0 and grid[u-1][v] == 1 and (u-1, v) not in visited:
                q.append((u-1, v, t+1))
                visited.add((u-1, v))
                rottenOranges += 1

        print(totalOranges, rottenOranges)
        if rottenOranges != totalOranges:
            return -1

        return totalMinutes