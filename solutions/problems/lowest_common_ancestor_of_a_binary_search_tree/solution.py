# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None

        if p.val <= root.val and root.val <= q.val or q.val <= root.val and root.val <= p.val:
            return root

        if p.val < root.val and q.val < root.val or q.val < root.val and p.val < root.val:
            found = self.lowestCommonAncestor(root.left, p, q)
            if found is not None:
                return found
        elif p.val > root.val and q.val > root.val or q.val < root.val and p.val < root.val:
            found = self.lowestCommonAncestor(root.right, p, q)
            if found is not None:
                return found
        elif p.val == root.val or q.val == root.val:
            return root

        return None