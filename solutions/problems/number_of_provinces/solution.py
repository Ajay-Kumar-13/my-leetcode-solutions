class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        roots = {}

        for i in range(1, len(isConnected)+1):
            roots[i] = i

        def findRoot(x):

            while x != roots.get(x):
                x = roots.get(x)

            return x

        edges = 0

        for i,edge in enumerate(isConnected):
            left = 0
            right = 0
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not left:
                    left = j + 1
                elif isConnected[i][j] == 1 and not right:
                    right = j + 1

                if left and right:
                    x = findRoot(left)
                    y = findRoot(right)

                    if x != y:
                        edges += 1

                    roots[x] = y
                    left = right
                    right = 0

        return len(isConnected) - edges