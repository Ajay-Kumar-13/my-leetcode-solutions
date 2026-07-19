# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        temp = root.right
        
        root.right = root.left
        root.left = None

        self.flatten(root.right)

        temp2 = root
        while temp2.right:
            temp2 = temp2.right
        
        temp2.right = temp

        self.flatten(temp)