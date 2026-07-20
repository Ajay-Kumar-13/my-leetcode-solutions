from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        total_oranges = 0

        rottenOranges = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total_oranges += 1
                if grid[i][j] == 2:
                    rottenOranges.append([i, j, 0])

        processedOranges = 0

        min_time = 0

        while len(rottenOranges) > 0:
            i, j, t = rottenOranges.popleft()
            processedOranges += 1
            min_time = max(min_time, t)
            if i < m-1 and grid[i+1][j] == 1:
                rottenOranges.append([i+1, j, t+1])
                grid[i+1][j] = 2
            if j < n-1 and grid[i][j+1] == 1:
                rottenOranges.append([i, j+1, t+1])
                grid[i][j+1] = 2
            if i > 0 and grid[i-1][j] == 1:     
                rottenOranges.append([i-1, j, t+1])
                grid[i-1][j] = 2
            if j > 0 and grid[i][j-1] == 1:
                rottenOranges.append([i, j-1, t+1])
                grid[i][j-1] = 2

        if processedOranges == total_oranges:
            return min_time

        return -1