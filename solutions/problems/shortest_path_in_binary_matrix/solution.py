from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([[0, 0, 1]])

        visited = set((0,0))

        shortest_path = float('inf')
        
        while len(q) > 0:
            x, y, path = q.popleft()
           
            if x == n-1 and y == n-1:
                shortest_path = min(shortest_path, path)

            if x < n-1 and y < n-1 and grid[x+1][y+1] == 0 and (x+1, y+1) not in visited:
                q.append((x+1, y+1, path+1))
                visited.add((x+1,y+1))
            if x > 0 and y > 0 and grid[x-1][y-1] == 0 and (x-1, y-1) not in visited:
                q.append((x-1, y-1, path+1))
                visited.add((x-1,y-1))
            if x > 0 and y < n-1 and grid[x-1][y+1] == 0 and (x-1, y+1) not in visited:
                q.append((x-1, y+1, path+1))
                visited.add((x-1,y+1))
            if x < n-1 and y > 0 and grid[x+1][y-1] == 0 and (x+1, y-1) not in visited:
                q.append((x+1, y-1, path+1))
                visited.add((x+1,y-1))

            if y < n-1 and grid[x][y+1] == 0 and (x, y+1) not in visited:
                q.append((x, y+1, path+1))
                visited.add((x,y+1))
            if x > 0 and grid[x-1][y] == 0 and (x-1, y) not in visited:
                q.append((x-1, y, path+1))
                visited.add((x-1,y))
            if x < n-1 and grid[x+1][y] == 0 and (x+1, y) not in visited:
                q.append((x+1, y, path+1))
                visited.add((x+1,y))
            if y > 0 and grid[x][y-1] == 0 and (x, y-1) not in visited:  
                q.append((x, y-1, path+1))
                visited.add((x,y-1))

        if shortest_path == float('inf'):
            return -1

        return shortest_path