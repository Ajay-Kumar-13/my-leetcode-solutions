"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        nodes = {}

        root = Node(node.val)
        nodes[node.val] = root

        q = deque(node.neighbors)

        visited = set(map(lambda x: x.val, node.neighbors))

        while len(q) > 0:

            node = q.popleft()

            if node.val not in nodes:
                nodes[node.val] = Node(node.val)

            for child in node.neighbors:
                if child.val not in nodes:
                    nodes[child.val] = Node(child.val)
                
                parent = nodes.get(child.val)
                parent.neighbors.append(nodes.get(node.val))

                if child.val not in visited:
                    q.append(child)
                    visited.add(child.val)

        return root