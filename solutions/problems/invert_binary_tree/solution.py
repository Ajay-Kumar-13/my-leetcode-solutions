# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        leftNode = None
        if root.left:
            leftNode = self.invertTree(root.left)
        
        rightNode = None
        if root.right:
            rightNode = self.invertTree(root.right)
            
        root.left = rightNode
        root.right = leftNode
        
        return root