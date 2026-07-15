# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def countGoodNodes(self, root, count, target):

        if not root:
            return count

        if target < root.val:
            target = root.val
            count += 1
        elif target == root.val:
            count += 1

        count = self.countGoodNodes(root.left, count, target)
        count = self.countGoodNodes(root.right, count, target)
        return count


    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        return self.countGoodNodes(root, 0, root.val)