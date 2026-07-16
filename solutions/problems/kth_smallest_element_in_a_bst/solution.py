# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getKthSmallest(self, root, k, count):
        if root is None:
            return count, False
        count, found = self.getKthSmallest(root.left, k, count)
        if found:
            return count, True
        count += 1
        if count == k:
            return root.val, True
        count, found = self.getKthSmallest(root.right, k, count)
        if found:
            return count, True
        return count, False

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.getKthSmallest(root, k, 0)[0]