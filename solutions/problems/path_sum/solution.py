# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasSum(root, target, count):
            if root is None:
                return count
            
            count += root.val

            if target == count and root.left is None and root.right is None:
                return True

            if hasSum(root.left, target, count) is True:
                return True

            if hasSum(root.right, target, count) is True:
                return True

            return False
        
        if root is None:
            return False

        return hasSum(root, targetSum, 0)