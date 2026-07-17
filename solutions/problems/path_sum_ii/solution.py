# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPath(self, root, target, path, count, ans):
    
        if root is None:
            return ans

        count += root.val
        path.append(root.val)

        ans = self.hasPath(root.left, target, path, count, ans)
        ans = self.hasPath(root.right, target, path, count, ans)

        if count == target and root.left is None and root.right is None:
            ans.append(path[:])

        if len(path) > 0:
            path.pop()

        return ans

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.hasPath(root, targetSum, [], 0, [])