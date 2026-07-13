# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diameter = 0

    def getDiameter(self, root, count):
        if not root.left and not root.right:
            return (count)
        
        maxDepthOfLeftTree = 0
        if root.left:
            stats = self.getDiameter(root.left, count+1)
            maxDepthOfLeftTree = stats - count

        maxDepthOfRightTree = 0
        if root.right:
            stats = self.getDiameter(root.right, count+1)
            maxDepthOfRightTree = stats - count

        self.diameter = max(self.diameter, maxDepthOfLeftTree+maxDepthOfRightTree)

        return max(maxDepthOfLeftTree, maxDepthOfRightTree) + count

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        self.getDiameter(root, 0)

        return self.diameter