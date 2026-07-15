# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getLevelOrder(self, root, level, allElements):

        if not root:
            return allElements

        if level+1 > len(allElements):
            allElements.append([])

        allElements[level].append(root.val)

        allElements = self.getLevelOrder(root.left, level+1, allElements)

        allElements = self.getLevelOrder(root.right, level+1, allElements)

        return allElements


    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        return self.getLevelOrder(root, 0, [])