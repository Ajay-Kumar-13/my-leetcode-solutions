# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMaxDepth(self, root, count):

        if not root.left and not root.right:
            return count

        maxDepthOfLeftTree = 0
        if root.left:
            maxDepthOfLeftTree = self.getMaxDepth(root.left, count+1)

        maxDepthOfRightTree = 0
        if root.right:
            maxDepthOfRightTree = self.getMaxDepth(root.right, count+1)

        return max(maxDepthOfLeftTree, maxDepthOfRightTree)

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        return self.getMaxDepth(root, 1)