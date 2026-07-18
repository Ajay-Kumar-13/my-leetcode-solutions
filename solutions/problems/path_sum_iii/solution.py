# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    total = 0
    mappings = {}
    mappings[0] = 1

    def getCount(self, root, target, count):
        if root is None:
            return count

        count += root.val
        self.total += self.mappings.get(count - target, 0)
        self.mappings[count] = self.mappings.get(count, 0)+1

        count = self.getCount(root.left, target, count)
        
        count = self.getCount(root.right, target, count)

        self.mappings[count] = self.mappings.get(count, 0)-1
        count -= root.val
        
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.getCount(root, targetSum, 0)
        return self.total