from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        q = deque([(0, 0, 1)])

        n = len(grid)

        visited = set((0, 0))

        while len(q) > 0:

            i, j, path = q.popleft()

            if i == n-1 and j == n-1:
                return path

            if i < n-1 and j < n-1 and grid[i+1][j+1] == 0 and (i+1, j+1) not in visited:
                visited.add((i+1, j+1))
                q.append((i+1, j+1, path+1))

            if j < n-1 and grid[i][j+1] == 0 and (i, j+1) not in visited:
                visited.add((i, j+1))
                q.append((i, j+1, path+1))

            if i < n-1 and grid[i+1][j] == 0 and (i+1, j) not in visited:
                visited.add((i+1, j))
                q.append((i+1, j, path+1))

            if i > 0 and j < n-1 and grid[i-1][j+1] == 0 and (i-1, j+1) not in visited:
                visited.add((i-1, j+1))
                q.append((i-1, j+1, path+1))

            if i > 0 and grid[i-1][j] == 0 and (i-1, j) not in visited:
                visited.add((i-1, j))
                q.append((i-1, j, path+1))

            if i > 0 and j > 0 and grid[i-1][j-1] == 0 and (i-1, j-1) not in visited:
                visited.add((i-1, j-1))
                q.append((i-1, j-1, path+1))

            if j > 0 and grid[i][j-1] == 0 and (i, j+1) not in visited:
                visited.add((i, j-1))
                q.append((i, j-1, path+1))

            if i < n-1 and j > 0 and grid[i+1][j-1] == 0 and (i+1, j-1) not in visited:
                visited.add((i+1, j-1))
                q.append((i+1, j-1, path+1))
        
        return -1