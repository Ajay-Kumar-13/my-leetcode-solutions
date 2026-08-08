class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        roots = {}
        for i in range(1, len(edges)+1):
            roots[i] = i

        def findRoot(r):
            while roots.get(r) != r:
                r = roots.get(r)

            return r


        for edge in edges:
            x = findRoot(edge[0])
            y = findRoot(edge[1])

            if x != y:
                roots[x] = y
            else:
                return edge