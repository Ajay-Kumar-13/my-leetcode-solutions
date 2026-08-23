# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getDepth(root):
            if root is None:
                return 0, True
            
            L, LB = getDepth(root.left)
            L += 1

            if not LB:
                return (0, LB)

            R, RB = getDepth(root.right)
            R += 1

            if not RB:
                return (0, RB)
            
            return (max(L, R), abs(L-R) <= 1)
        
        return getDepth(root)[1]