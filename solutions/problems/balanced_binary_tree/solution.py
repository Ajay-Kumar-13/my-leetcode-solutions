# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isHeightBalanced(self, root, height):
        
        isBalanced = True
        if not root.left and not root.right:
            return (height, True)

        leftNodeHeight = height
        if root.left:
            leftNodeHeight, isBalanced = self.isHeightBalanced(root.left, height+1)
            if not isBalanced:
                return (0, False)

        rightNodeHeight = height
        if root.right:
            rightNodeHeight, isBalanced = self.isHeightBalanced(root.right, height+1)
            if not isBalanced:
                return (0, False)

        balance = rightNodeHeight-leftNodeHeight
        if balance == 1 or balance == -1 or balance == 0:
            isBalanced = True
        else:
            isBalanced = False

        return (max(rightNodeHeight, leftNodeHeight), isBalanced)

        

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if not root:
            return True

        height, isBalanced = self.isHeightBalanced(root, 0)

        return isBalanced