class Solution:
    def findCircleNum(self, isConnected):
        
        roots = {}
        
        for i in range(len(isConnected)):
            roots[i] = i
            
        def findRoot(x):
            if x == roots.get(x):
                return x
                
            return findRoot(roots.get(x))
            
        m = len(isConnected)
        n = len(isConnected[0])
        
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    x = findRoot(i)
                    y = findRoot(j)

                    roots[y] = x
                    
        for k, v in roots.items():
            roots[k] = findRoot(v)
            
        return len(set(roots.values()))