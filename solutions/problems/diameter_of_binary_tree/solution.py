# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameter(self, root, count, maxPath):

        if root is None:
            return (0, maxPath)

        left, maxPath = self.diameter(root.left, count+1, maxPath)
        right, maxPath = self.diameter(root.right, count+1, maxPath)

        return (max(left+1, right+1), max(maxPath, left+right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        return self.diameter(root, 0, 0)[1]

        