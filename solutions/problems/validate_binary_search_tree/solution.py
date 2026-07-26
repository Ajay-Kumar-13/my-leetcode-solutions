# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, root, left, right):

        if not root:
            return True

        if root.val <= left or root.val >= right:
            return False

        if not self.isValid(root.left, left, root.val):
            return False

        if not self.isValid(root.right, root.val, right):
            return False

        return True

        
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.isValid(root, -float('inf'), float('inf'))