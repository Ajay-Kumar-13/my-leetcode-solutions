class Solution:

    def pathSum(self, root, targetSum):

        ans  = []

        def getTargetPathSums(root, target, path):
            
            if root is None:
                return 

            path.append(root.val)
            
            if root.left is None and root.right is None:
                if root.val == target:
                    ans.append(path[:])

            getTargetPathSums(root.left, target-root.val, path)
            getTargetPathSums(root.right, target-root.val, path)
            
            path.pop()

            return path
        
        getTargetPathSums(root, targetSum, [])
        
        return ans