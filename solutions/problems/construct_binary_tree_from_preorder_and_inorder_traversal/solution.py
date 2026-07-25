# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        inorder_ind = {}

        for i in range(len(preorder)):
            inorder_ind[inorder[i]] = i

        def insert(root, val, left, mid, right):

            if not root:
                return TreeNode(val)

            position = inorder_ind.get(val)

            if position < mid and position >= left:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root
                if insert(root.left, val, left, inorder_ind.get(root.left.val) ,mid):
                    return root
            
            if position > mid and position <= right:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root
                if insert(root.right, val, mid, inorder_ind.get(root.right.val) ,right):
                    return root

            return root


        
        root = None

        for i in range(len(preorder)):
            rootPos = inorder_ind.get(preorder[0])
            root = insert(root, preorder[i], 0, rootPos, len(preorder)-1)

        return root