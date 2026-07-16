# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValid(self, root, left, right):

        if not root:
            return True

        if left >= root.val or right <= root.val:
            return False

        return self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if not root:
            return True

        return self.isValid(root, -float('inf'), float('inf'))