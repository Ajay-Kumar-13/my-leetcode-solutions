class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        roots = {}

        # DSU - Disjoint Set Union

        def findRoot(x):
            while x != roots.get(x):
                x = roots.get(x)
            return x
        
        for i in range(1,len(edges)+1):
            roots[i] = i

        for edge in edges:
            
            x = edge[0]
            y = edge[1]

            xRoot = findRoot(x)
            yRoot = findRoot(y)

            if xRoot == yRoot:
                return edge

            roots[xRoot] = yRoot