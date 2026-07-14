# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def checkTree(self, p, q):

        if not p and not q:
            return True

        if p and not q or q and not p:
            return False

        if p.val != q.val:
            return False
        
        left = self.checkTree(p.left, q.left)
        if not left:
            return False

        right = self.checkTree(p.right, q.right)
        if not right:
            return False
        
        return True


    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root and subRoot or not subRoot and root:
            return False

        if not root and not subRoot:
            return True

        if root.val == subRoot.val:
            if self.checkTree(root, subRoot):
                return True
        
        isSubTree = self.isSubtree(root.left, subRoot)
        if isSubTree:
            return True

        isSubTree = self.isSubtree(root.right, subRoot)
        if isSubTree:
            return True

        return False