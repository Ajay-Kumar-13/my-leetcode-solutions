# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    maxSum = -float('inf')

    def findMaxPathSum(self, root):
        if not root:
            return 0

        leftSum = self.findMaxPathSum(root.left)

        rightSum = self.findMaxPathSum(root.right)

        maxInNode = max(root.val+leftSum, root.val+rightSum, root.val+leftSum+rightSum, root.val)
        
        self.maxSum = max(self.maxSum, maxInNode)

        return max(root.val+leftSum, root.val+rightSum, root.val)


    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.findMaxPathSum(root)
        return self.maxSum