"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # BFS
        q = deque([node])

        nodes = {} 

        while len(q) > 0:
            currentNode = q.popleft()

            nd = nodes.get(currentNode.val, None)

            if not nd:
                nd = Node(currentNode.val, [])
                nodes[currentNode.val] = nd

            for n in currentNode.neighbors:
                
                neighbourNode = nodes.get(n.val, None)
                if not neighbourNode:
                    neighbourNode = Node(n.val, [])    
                    nodes[neighbourNode.val] = neighbourNode
                    q.append(n)
                
                nd.neighbors.append(neighbourNode)

        return nodes[node.val]
