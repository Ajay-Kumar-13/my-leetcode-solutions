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

        inOrderIndex = {}
        for i in range(len(inorder)):
            inOrderIndex[inorder[i]] = i

        def insert(root, node, left, right):
            newIndex = inOrderIndex.get(node.val)
            index = inOrderIndex.get(root.val)
            if newIndex >= left and newIndex < index:
                if not root.left:
                    root.left = node
                    return root
                if insert(root.left, node, left, index):
                    return
            
            if newIndex > index and newIndex <= right:
                if not root.right:
                    root.right = node
                    return root
                if insert(root.right, node, index, right):
                    return

            return None 

        left = 0
        right = len(inorder) - 1

        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            newNode = TreeNode(preorder[i])
            insert(root, newNode, left, right)

        return root