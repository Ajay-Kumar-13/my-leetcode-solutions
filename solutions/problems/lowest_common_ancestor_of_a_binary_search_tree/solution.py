# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def getLowestCommonAncestor(self, root, p, q):
        
        if root is None:
           return None
        print(root.val)
        if root is p or root is q:
            return root

        left = self.getLowestCommonAncestor(root.left, p, q)
        # if left:
        #     return left

        right = self.getLowestCommonAncestor(root.right, p, q)
        # if right:
        #     return right

        if left and right:
            return root
            
        if left:
            return left

        if right:
            return right

        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.getLowestCommonAncestor(root, p, q)
        